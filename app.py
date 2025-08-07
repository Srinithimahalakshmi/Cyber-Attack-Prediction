from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load model and encoders
model = joblib.load('model.joblib')
label_encoders = joblib.load('label_encoders.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            int(request.form['network_packet_size']),
            request.form['protocol_type'],
            int(request.form['login_attempts']),
            float(request.form['session_duration']),
            request.form['encryption_used'],
            float(request.form['ip_reputation_score']),
            int(request.form['failed_logins']),
            request.form['browser_type'],
            int(request.form['unusual_time_access'])
        ]

        # Encode categorical fields
        features[1] = label_encoders['protocol_type'].transform([features[1]])[0]
        features[4] = label_encoders['encryption_used'].transform([features[4]])[0]
        features[7] = label_encoders['browser_type'].transform([features[7]])[0]

        prediction = model.predict([features])[0]
        result = "High Risk" if prediction == 1 else "Low Risk"

        return render_template('index.html', prediction_text=f"Predicted Risk Level: {result}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
