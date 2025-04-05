import warnings
warnings.filterwarnings("ignore")
import os

os.environ["OPENBLAS_NUM_THREADS"] = "4"
os.environ["NUMEXPR_NUM_THREADS"] = "4"
os.environ["OMP_NUM_THREADS"] = "4"

import torch
from deoldify.visualize import get_image_colorizer
from PIL import Image, ImageEnhance
import mediapipe as mp
import cv2

bw_image_path = "test_images/man.jpg"
output_dir = "result_images"
os.makedirs(output_dir, exist_ok=True)

default_render_factor = 35
face_render_factor = 26
min_render_factor = 20
colorizer = get_image_colorizer(artistic=True)

image_cv2 = cv2.imread(bw_image_path)
image_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)

has_face = False

with mp.solutions.face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.3) as detector:
    detection_results = detector.process(image_rgb)
    if detection_results.detections:
        has_face = True
        
if not has_face:
    with mp.solutions.face_mesh.FaceMesh(
        static_image_mode=True,
        max_num_faces=5,
        refine_landmarks=True,
        min_detection_confidence=0.3
    ) as face_mesh:
        mesh_results = face_mesh.process(image_rgb)
        if mesh_results.multi_face_landmarks:
            has_face = True

if has_face:
    render_factor = face_render_factor
    enhance_color = False
    print("Приступаем..")
else:
    render_factor = default_render_factor
    enhance_color = True
    print("Одну секунду!")

print("🎨 Раскрашиваем изображение...")
colorized = None

while render_factor >= min_render_factor:
    try:
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

        colorized = colorizer.get_transformed_image(
            path=bw_image_path,
            render_factor=render_factor
        )
        break
    except RuntimeError:
        print(f"⚠️ OOM при render_factor={render_factor}, уменьшаем...")
        render_factor -= 5
else:
    print("❌ Не удалось раскрасить изображение.")
    exit()

if enhance_color:
    enhancer = ImageEnhance.Color(colorized)
    colorized = enhancer.enhance(2)

filename = os.path.splitext(os.path.basename(bw_image_path))[0]
colorized_path = os.path.join(output_dir, f"{filename}_colorized.jpg")
colorized.save(colorized_path)

bw_image = Image.open(bw_image_path).convert("RGB").resize(colorized.size)
comparison = Image.new("RGB", (bw_image.width * 2, bw_image.height))
comparison.paste(bw_image, (0, 0))
comparison.paste(colorized, (bw_image.width, 0))

comparison_path = os.path.join("./comparison_images", f"{filename}_comparison.jpg")
comparison.save(comparison_path)

print(f"📸 Готово!\n- Цветное: {colorized_path}\n- Сравнение: {comparison_path}")
