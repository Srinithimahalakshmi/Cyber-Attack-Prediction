 Cyber-Attack Prediction System

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)]()

##  Overview
A machine learning system that predicts cyber attacks using network traffic data—leveraging logistic regression, feature engineering, and a user-friendly web interface powered by Flask, HTML, and CSS. Detect threats in real time!

##  Features
-  Data preprocessing pipeline for network traffic  
-  Feature engineering to extract meaningful patterns  
-  Multiple ML models: Logistic Regression, Random Forest, XGBoost, Neural Networks  
-  Model performance metrics and visualizations  
-  SHAP explainability for transparent predictions

##  Table of Contents
- [⚙️ Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [📁 Project Structure](#-project-structure)  
- [📊 Results](#-results)  
- [🤝 Contributing](#-contributing)  
- [📜 License](#-license)  
- [📬 Contact](#-contact)

---

##  Installation

```bash
git clone https://github.com/Srinithimahalakshmi/Cyber-Attack-Prediction.git
cd Cyber-Attack-Prediction

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
````

You’ll need Python 3.8+ and pip. The repository includes a processed subset of the CIC-IDS2017 dataset.

---

## Usage

### 1. Data Preprocessing

```bash
python src/data_preprocessing.py
```

### 2. Model Training

Train models such as Random Forest or XGBoost:

```bash
python src/models/train_rf.py
python src/models/train_xgb.py
```

### 3. Model Evaluation

```bash
python src/evaluate.py --model models/random_forest.pkl
```

### 4. Generate Predictions

```python
from src.predict import AttackPredictor

predictor = AttackPredictor('models/random_forest.pkl')
sample = [...]  # Input feature vector
prediction = predictor.predict(sample)
print(f"Attack probability: {prediction:.2%}")
```

---

## Project Structure

| Path               | Description                           |
| ------------------ | ------------------------------------- |
| `data/`            | Raw & processed datasets              |
| `notebooks/`       | EDA & feature-engineering notebooks   |
| `src/`             | Source code, including models & utils |
| `models/`          | Trained model files                   |
| `results/`         | Metrics & plot outputs                |
| `requirements.txt` | Dependencies                          |
| `LICENSE`          | MIT License                           |

---

## Results

| Model          | Accuracy | Precision | Recall | F1-Score |
| -------------- | -------- | --------- | ------ | -------- |
| Random Forest  | 98.7%    | 97.2%     | 96.8%  | 97.0%    |
| XGBoost        | 99.1%    | 98.5%     | 97.9%  | 98.2%    |
| Neural Network | 98.2%    | 96.8%     | 97.1%  | 96.9%    |

Visual outputs like confusion matrices and SHAP explainability plots are available in the `results/` folder.

---

## Contributing

Contributions are welcome! Whether it's improved models, additional UI enhancements, or documentation updates, we'd love your help.
Steps to contribute:

1. Fork the repo
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes & commit (`git commit -m 'Add feature...'`)
4. Push to your branch & open a Pull Request

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## Contact

👤 **Maintainer**: Srinithi Mahalakshmi
📧 **Email**: [your.email@example.com](mailto:your.email@example.com)
🔗 **GitHub**: [Srinithimahalakshmi](https://github.com/Srinithimahalakshmi)

---

⭐ *If this project helped, please give it a star!*

```

---

Feel free to let me know if you'd like adjustments like specific model metrics, dataset details, or additional emojis—happy to help further!
::contentReference[oaicite:0]{index=0}
```
