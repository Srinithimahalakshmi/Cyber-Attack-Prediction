# Cyber Attack Prediction System 🛡️

![Cyber Security](https://img.shields.io/badge/domain-cybersecurity-blue) ![Machine Learning](https://img.shields.io/badge/ML-Classification-green) ![Python](https://img.shields.io/badge/Python-3.8%2B-yellow)

Machine learning system for predicting cyber attacks using network traffic data. Includes data preprocessing, feature engineering, and multiple classification models.

## Features ✨
- Data preprocessing pipeline for network traffic data
- Feature engineering for security-relevant patterns
- Multiple ML models (Random Forest, XGBoost, Neural Networks)
- Model evaluation metrics and visualization
- SHAP explainability for attack predictions

## Installation 🚀

### Prerequisites
- Python 3.8+
- pip package manager

### Setup
```bash
# Clone repository
git clone https://github.com/Srinithimahalakshmi/Cyber-Attack-Prediction.git
cd Cyber-Attack-Prediction

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
Dataset 📊
CIC-IDS2017 Dataset - Contains benign and common attack network flows

Included in data/ directory

Features:

Flow duration

Packet size statistics

Protocol information

Flag counts

Attack types:

DDoS

PortScan

Brute Force

Web Attacks

Usage 🧪
1. Data Preprocessing
bash
python src/data_preprocessing.py
2. Model Training
bash
# Train Random Forest model
python src/models/train_rf.py

# Train XGBoost model
python src/models/train_xgb.py
3. Model Evaluation
bash
python src/evaluate.py --model models/random_forest.pkl
4. Generate Predictions
python
from src.predict import AttackPredictor

predictor = AttackPredictor('models/random_forest.pkl')
sample = [...]  # Input feature vector
prediction = predictor.predict(sample)
print(f"Attack probability: {prediction}")
Results 📈
Model	Accuracy	Precision	Recall	F1-Score
Random Forest	98.7%	97.2%	96.8%	97.0%
XGBoost	99.1%	98.5%	97.9%	98.2%
Neural Network	98.2%	96.8%	97.1%	96.9%
https://results/confusion_matrix.png

Repository Structure 📂
text
├── data/                   # Raw and processed datasets
│   ├── raw/                # Original CIC-IDS2017 data
│   └── processed/          # Preprocessed datasets
│
├── notebooks/              # Exploratory analysis notebooks
│   ├── EDA.ipynb
│   └── Feature_Engineering.ipynb
│
├── src/                    # Source code
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── evaluate.py
│   ├── predict.py
│   └── models/             # Model training scripts
│       ├── train_rf.py
│       ├── train_xgb.py
│       └── train_nn.py
│
├── models/                 # Saved model files
├── results/                # Evaluation metrics and plots
├── requirements.txt        # Python dependencies
└── LICENSE
Key Files 🔑
notebooks/EDA.ipynb - Exploratory data analysis

src/data_preprocessing.py - Data cleaning pipeline

src/feature_engineering.py - Feature creation module

src/models/train_xgb.py - XGBoost training script

src/predict.py - Prediction interface

Contributing 🤝
Contributions are welcome! Please follow these steps:

Fork the repository

Create a new branch (git checkout -b feature/your-feature)

Commit changes (git commit -am 'Add new feature')

Push to branch (git push origin feature/your-feature)

Open a pull request

License 📄
This project is licensed under the MIT License - see LICENSE file for details.

Contact 📬
Srinithi Mahalakshmi
https://img.shields.io/badge/LinkedIn-Connect-blue
https://img.shields.io/badge/GitHub-Follow-lightgrey
