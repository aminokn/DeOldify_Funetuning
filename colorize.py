import warnings
warnings.filterwarnings("ignore")

from deoldify.visualize import get_image_colorizer
from PIL import ImageEnhance
import os

# === Пути ===
bw_image_path = "test_images/istockphoto-1403500817-612x612.jpg"
output_dir = "result_images"
os.makedirs(output_dir, exist_ok=True)

# === Настройки ===
render_factor = 45
enhance_color = True

# === Раскрашивание ===
colorizer = get_image_colorizer(artistic=True)
print("🎨 Раскрашиваем изображение...")

colorized = colorizer.get_transformed_image(
    path=bw_image_path,
    render_factor=render_factor
)

# === Усиление насыщенности ===
if enhance_color:
    enhancer = ImageEnhance.Color(colorized)
    colorized = enhancer.enhance(2)  

# === Получаем имя файла (без расширения) ===
filename = os.path.splitext(os.path.basename(bw_image_path))[0]
output_filename = f"{filename}_colorized.jpg"
output_path = os.path.join(output_dir, output_filename)

# === Сохраняем ===
colorized.save(output_path)
print(f"✅ Готово! Сохранено в: {output_path}")
