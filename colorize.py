import warnings
warnings.filterwarnings("ignore")

from deoldify.visualize import get_image_colorizer
from PIL import ImageEnhance
import os
import torch

bw_image_path = "test_images/mountain-countryside-landscape-at-sunset-dramatic-sky-over-a-distant-valley-green-fields-and-trees-on-hill-beautiful-natural-landscapes-of-the-carpathians-generative-ai-variation-5-photo.jpg"
output_dir = "result_images"
os.makedirs(output_dir, exist_ok=True)

initial_render_factor = 40
min_render_factor = 20
enhance_color = True

colorizer = get_image_colorizer(artistic=True)
print("🎨 Раскрашиваем изображение...")

render_factor = initial_render_factor
colorized = None

while render_factor >= min_render_factor:
    try:
        torch.cuda.empty_cache() if torch.cuda.is_available() else None
        colorized = colorizer.get_transformed_image(
            path=bw_image_path,
            render_factor=render_factor
        )
        print(f"✅ Успех с render_factor={render_factor}")
        break 
    except RuntimeError as e:
        print(f"⚠️ OOM при render_factor={render_factor}, уменьшаем...")
        render_factor -= 5
else:
    print("❌ Не удалось раскрасить изображение. Попробуйте позже или уменьшите размер.")

if colorized and enhance_color:
    enhancer = ImageEnhance.Color(colorized)
    colorized = enhancer.enhance(2)

if colorized:
    filename = os.path.splitext(os.path.basename(bw_image_path))[0]
    output_filename = f"{filename}_colorized.jpg"
    output_path = os.path.join(output_dir, output_filename)

    colorized.save(output_path)
    print(f"✅ Готово! Сохранено в: {output_path}")

