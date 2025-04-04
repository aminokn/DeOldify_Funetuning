from fastai.vision.all import *
import os

# === Пути ===
bw_path = "dataset/train/bw"
color_path = "dataset/train/color"

# === DataBlock ===
def get_dls(bw_path, color_path, bs=4, size=256):
    def label_func(x): return Path(color_path)/x.name

    block = DataBlock(
        blocks=(ImageBlock(cls=PILImageBW), ImageBlock),
        get_items=get_image_files,
        get_y=label_func,
        splitter=RandomSplitter(0.1),  # 10% валидация
        item_tfms=Resize(size),
        batch_tfms=aug_transforms()
    )

    return block.dataloaders(bw_path, bs=bs)

# === Загрузка данных ===
dls = get_dls(bw_path, color_path)

# === Обучение U-Net с ResNet34 ===
learn = unet_learner(
    dls, resnet34,
    loss_func=F.mse_loss,  # можно заменить на SSIM Loss или VGG perceptual
    metrics=PSNR()
)

# === Обучение ===
learn.fine_tune(10)

# === Сохраняем ===
learn.export('colorizer_custom.pkl')
print("✅ Модель сохранена как colorizer_custom.pkl")
