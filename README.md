
# Diabetes Dashboard Project

This project is a diabetes prediction and explanation tool built using:
- A trained Random Forest model
- SHAP for explainability
- Streamlit for the dashboard

## 📁 Folder Structure

```
Diabetes_Dashboard_Project/
├── Di_2025.ipynb               # Jupyter notebook for model training and SHAP
├── dashboard.py                # Streamlit dashboard app
├── requirements.txt            # Dependencies
├── model/                      # Trained model and scaler (pkl files)
├── images/                     # Visualizations (e.g. SHAP, Feature Importance)
└── data/                       # Your dataset (e.g. diabetes.csv)
```

## 🚀 Getting Started

```bash
cd Diabetes_Dashboard_Project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run dashboard.py
```

## 🔧 Inputs for Prediction

- Glucose
- BMI
- Age
- Insulin

## 📊 Outputs

- Diabetes prediction
- SHAP feature importance plot
- Feature importance plot
