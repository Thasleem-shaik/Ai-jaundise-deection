---
name: update-project-readme
description: it iwll update the project-level README for the AI Jaundice Detection project
---
# Skill: Update Project README

Use this file to guide the project-level README update for the AI Jaundice Detection project.

## Project overview
This project is an educational AI-based application for screening possible signs of jaundice from eye images. The system captures a photo of the eye using a webcam or uploaded image, processes the image, and uses a trained model to analyze the sclera and surrounding eye region to identify whether jaundice may be present.

Important note: This is a learning/demo project and is not a medical diagnosis tool. It should be used only for educational or research purposes.

## What the project is about
- AI-powered jaundice screening from eye images
- Image capture using webcam via Streamlit
- Eye and sclera preprocessing using OpenCV and image processing utilities
- Model inference using a trained Keras/TensorFlow model
- Educational and prototype-level screening workflow

## Technologies used
The project uses the following technologies:
- Python 3.10+
- Streamlit for the web UI
- TensorFlow / Keras for model training and inference
- OpenCV for image processing and eye detection
- Pillow (PIL) for image handling
- NumPy and pandas for numerical/data processing
- scikit-learn for evaluation-related preprocessing and model utilities
- Matplotlib for visualizations and analysis
- Git for version control

## Project structure
- `app.py` – main Streamlit application
- `training/` – model training and evaluation scripts
- `detection/` – eye and sclera detection logic
- `utils/` – image processing and prediction helpers
- `model/` – trained model and class list
- `assets/` – UI-related media files
- `requirements.txt` – Python dependencies

## Prerequisites
Before running the project locally, make sure you have:
- Python 3.10 or newer installed
- `pip` available
- A virtual environment tool such as `venv`
- Git installed
- Webcam access for live image capture (optional if using uploaded images)
- A system with enough RAM for model inference; 8 GB+ is recommended

## Local setup instructions
Run the following commands from the project root:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Ai-jaundise-deection
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open the URL shown by Streamlit in the browser (usually `http://localhost:8501`).

## Expected local workflow
- Launch the app
- Allow webcam access if prompted
- Capture an image of the eye
- Click the analyze button
- Review the AI screening result shown by the interface

## README content checklist
When updating the project-level README, include these sections:
- Project title
- Short project summary
- Problem statement or use case
- Features
- Technologies used
- Prerequisites
- Local setup steps
- Run instructions
- Folder structure
- Notes for educational use
- Screenshot or demo section if available

## Recommended README tone
Write the README in a professional, beginner-friendly style. Keep it clear, concise, and practical. Focus on installation, technology stack, and local usage steps.

## Example README summary
```md
# AI Jaundice Detection

This project is an educational AI-based application designed to detect possible signs of jaundice using eye images. It uses image processing and a trained deep learning model to analyze the eye and sclera region for screening purposes.

## Technologies
- Python
- Streamlit
- TensorFlow/Keras
- OpenCV
- PIL
- NumPy
- scikit-learn

## Prerequisites
- Python 3.10+
- pip
- Git
- Webcam access

## Local run
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Note
This project is intended for educational and research use only and is not a medical diagnosis tool.
```

## Final instruction
Update the root README so it clearly explains what the project does, the technologies involved, what prerequisites are required, and how to start the app locally in a simple step-by-step format.
