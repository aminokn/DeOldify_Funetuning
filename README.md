# 🎨 Custom DeOldify Colorizer (KBTU)

This is a customized version of **DeOldify**, fine-tuned on a proprietary dataset of grayscale and color image pairs as part of a diploma project at **Kazakh-British Technical University (KBTU)**.

> 🎯 Goal: Improve the quality of automatic colorization for historical and archival photographs.
---

## 🧠 Model Architecture

| Component         | Description                        |
|------------------ |------------------------------------|
| 📦 Architecture   | `FastAI` + `U-Net` + `ResNet34`    |
| 🧠 Framework      | `fastai v1`                        |
| 🎯 Loss Function  | `VGGPerceptualLoss`                |
| 📈 Metric         | `PSNR`                             |
| 🖼 Dataset Size   | 2000+ grayscale/color image pairs from Unsplash |
| 🪄 Use Case       | Automatic photo colorization       |

---
## 📌 Key Features

✅ Detects faces on images using MediaPipe FaceMesh (even partially visible ones)  
✅ Dynamically adjusts `render_factor` and color enhancement  
✅ Fine-tuned DeOldify model for portrait colorization  
✅ Generates side-by-side comparison (before/after)

## 🚀 Quick Start
### 1. Clone the repo

```
git clone https://github.com/aminokn/DeOldify_Funetuning.git
cd DeOldify_Funetuning
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Download the model weights
📦 Hugging Face Model: aminokn/colorizer-model

```
wget https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth 
wget (https://huggingface.co/aminokn/colorizer-model/resolve/main/colorizer_vgg_fastai1.pkl)
```
### 4. Run the colorizer
```
python colorize.py
```

### 📁 Project Structure
```
DeOldify_Funetuning/
├── dataset/             # Training images (bw / color)
├── models/              # Trained model weights (.pth / .pkl)
├── colorize.py          # Inference script
├── train_v2.py          # Training script
└── README.md            # This file 🌟
```
### 🖼️ Example Results
#### Before/After Colorization
![comparison_images/bird-8788491_1280_comparison.jpg](https://github.com/aminokn/DeOldify_Funetuning/blob/master/comparison_images/bird-8788491_1280_comparison.jpg)
![comparison_images/elephant_comparison.jpg](https://github.com/aminokn/DeOldify_Funetuning/blob/master/comparison_images/elephant_comparison.jpg)
![comparison_images/nature-3_comparison.jpg](https://github.com/aminokn/DeOldify_Funetuning/blob/master/comparison_images/nature-3_comparison.jpg)
![comparison_images/heaven_comparison.jpg](https://github.com/aminokn/DeOldify_Funetuning/blob/master/comparison_images/heaven_comparison.jpg)
![comparison_images/horse%20comparison.jpeg](https://github.com/aminokn/DeOldify_Funetuning/blob/master/comparison_images/horse%20comparison.jpeg)
![comparison_images/jaguar.jpeg](https://github.com/aminokn/DeOldify_Funetuning/blob/master/comparison_images/jaguar.jpeg)
![comparison_images/man_comparison.jpg](https://github.com/aminokn/DeOldify_Funetuning/blob/master/comparison_images/man_comparison.jpg)
![comparison_images/nature.jpeg](https://github.com/aminokn/DeOldify_Funetuning/blob/master/comparison_images/nature.jpeg)
![comparison_images/tools-feature_black-and-white-filter_promo-showcase_01-AFTER4x_comparison.jpg](https://github.com/aminokn/DeOldify_Funetuning/blob/master/comparison_images/tools-feature_black-and-white-filter_promo-showcase_01-AFTER4x_comparison.jpg)
![comparison_images/woman%20with%20hat_comparison.jpg](https://github.com/aminokn/DeOldify_Funetuning/blob/master/comparison_images/woman%20with%20hat_comparison.jpg)

### 🤝 Authors
[aminokn](https://github.com/aminokn) – KBTU

🎓 Diploma Thesis: "Image Colorization via Web Application"

### 📄 License
Licensed under the MIT License.
