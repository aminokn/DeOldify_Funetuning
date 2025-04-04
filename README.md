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
| 🖼 Dataset Size   | 2000+ grayscale/color image pairs  |
| 🪄 Use Case       | Automatic photo colorization       |

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/aminokn/DeOldify_Funetuning.git
cd DeOldify_Funetuning

### 2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

### 3. Download the model weights
📦 Hugging Face Model: aminokn/colorizer-model

bash
Copy
Edit
wget https://huggingface.co/aminokn/colorizer-model/resolve/main/colorizer-v2.pkl -P ./models/

### 4. Run the colorizer
bash
Copy
Edit
python colorize.py

###📁 Project Structure
bash
Copy
Edit

### DeOldify_Funetuning/
├── dataset/             # Training images (bw / color)
├── models/              # Trained model weights (.pth / .pkl)
├── colorize.py          # Inference script
├── train_v2.py          # Training script
└── README.md            # This file 🌟

### 🖼️ Example Results
Coming soon... (or insert a preview grid of before/after images)

### 🤝 Authors
Aminokn – KBTU

🎓 Diploma Thesis: "Image Colorization via Web Application"

### 📄 License
Licensed under the MIT License.
