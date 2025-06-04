import streamlit as st
import numpy as np
import pandas as pd
import onnxruntime as rt
import joblib

# Load ONNX model and scaler
scaler = joblib.load("/Users/abhi/Desktop/Diabetes_Dashboard_Project/model/scaler.pkl")
sess = rt.InferenceSession("/Users/abhi/Desktop/Diabetes_Dashboard_Project/model/diabetes_model.onnx")
input_name = sess.get_inputs()[0].name

# UI
st.title("🩺 Diabetes Prediction Dashboard")

glucose = st.sidebar.slider("Glucose", 0, 200, 120)
bmi = st.sidebar.slider("BMI", 0.0, 70.0, 30.5)
age = st.sidebar.slider("Age", 10, 100, 25)
insulin = st.sidebar.slider("Insulin", 0, 300, 80)

if st.sidebar.button("Predict"):
    input_data = np.array([[glucose, bmi, age, insulin]])
    scaled_data = scaler.transform(input_data).astype(np.float32)
    output = sess.run(None, {input_name: scaled_data})[0]
    prediction = int(output[0])
    st.success(f"Prediction: **{'Diabetic' if prediction == 1 else 'Non-Diabetic'}**")
