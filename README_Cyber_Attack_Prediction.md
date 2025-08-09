# Cyber Attack Prediction Using Machine Learning

This project applies machine learning techniques to predict potential cyber attacks based on network traffic and system activity patterns.

## 📂 Project Structure

```
Cyber-Attack-Prediction/
│
├── data/
│   └── network_traffic.csv      # Dataset of network/system logs with attack labels
│
├── notebooks/
│   └── model_training.ipynb     # Notebook for preprocessing, training, and evaluation
│
├── model/
│   └── trained_model.pkl        # Serialized trained model
│
└── app.py                       # Flask application for serving live predictions
```

## 📊 Dataset Overview

Typically includes features such as:

- **timestamp**: Time of the measurement or event
- **source_ip**, **dest_ip**: Origin and destination of traffic
- **protocol**, **port**: Communication protocol and port number
- **feature_xxx**: Traffic statistics (packet size, duration, flags, etc.)
- **label**: Whether the record represents an attack or benign traffic

## 🤖 Machine Learning Algorithms

You may use one or more of the following:

- **Random Forest** – Handles high-dimensional data, provides feature importance
- **Support Vector Machine (SVM)** – Effective for binary classification with clear margins
- **Neural Networks** – Captures complex non-linear relationships in data

### Key Steps

1. **Data Preprocessing**  
   - Clean missing values  
   - Encode categorical features (e.g., protocol)  
   - Scale and normalize numerical features  
   - Handle class imbalance (e.g., SMOTE, undersampling)

2. **Feature Engineering**  
   - Extract temporal or statistical features  
   - Use aggregation and windowed statistics for richer patterns

3. **Model Training & Evaluation**  
   - Train multiple models  
   - Evaluate using accuracy, precision, recall, F1-score, ROC-AUC  
   - Select the best-performing model

4. **Deployment**  
   - Use Flask in `app.py` to serve model predictions  
   - Provide web interface to upload logs and receive attack predictions

## 📈 Accuracy & Results

- Best model achieved around **X% accuracy**, **Y precision**, **Z recall** on a held-out test set.  
- Feature importance analysis indicated that **feature A**, **feature B**, and **feature C** were the most predictive.

## 🚀 How to Run

```bash
git clone https://github.com/Srinithimahalakshmi/Cyber-Attack-Prediction.git
cd Cyber-Attack-Prediction
pip install -r requirements.txt
python app.py
```

Then open your browser and navigate to `http://127.0.0.1:5000` to interact with the prediction web service.

## 📚 References

- UCI Cyber Attack datasets (e.g., NSL-KDD, CICIDS-2017)  
- Scikit-learn documentation  
- Research on ensemble learning and network intrusion detection
