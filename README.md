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

1. Install dependencies:

```bash
pip install -r requirements.txt
Download the pre-trained model:

🔗 Hugging Face: aminokn/colorizer-model

bash
Copy
Edit
wget https://huggingface.co/aminokn/colorizer-model/resolve/main/colorizer-v2.pkl -P ./models/
Run inference:

bash
Copy
Edit
python colorize.py
📁 Project Structure
bash
Copy
Edit
DeOldify_Funetuning/
├── dataset/             # Dataset (bw / color images)
├── models/              # Model weights (.pth / .pkl)
├── colorize.py          # Inference script
├── train_colorizer.py   # Training script
└── README.md
📚 Authors
🧑 Aminokn (KBTU)

🎓 Diploma project: "Image Colorization via Web Application"

📝 License
MIT License
