
import streamlit as st
import pandas as pd

st.title("🤖 AI DiBOT - Ask Me Anything about Diabetes Prediction")

st.markdown("""
This assistant can help you understand common features, model choices, and performance metrics
related to diabetes prediction. Try asking things like:

- What is glucose?
- What is BMI?
- Explain ROC-AUC
- Which model is best?
- Why is Random Forest better?
- Is KNN a good model?
- What features are important?
""")

# Basic FAQ logic
def get_bot_response(question):
    q = question.lower()

    if "glucose" in q:
        return "Glucose is the amount of sugar in the blood. It is a key indicator of diabetes risk."
    elif "bmi" in q:
        return "BMI stands for Body Mass Index. It's a measure of body fat based on height and weight."
    elif "roc" in q or "auc" in q:
        return "ROC-AUC measures how well the model distinguishes between classes. Higher values mean better distinction."
    elif "best model" in q or "which model" in q:
        return "Random Forest is the best model based on accuracy and ROC-AUC in our testing."
    elif "random forest" in q and "better" in q:
        return "Random Forest is better because it combines multiple decision trees to reduce overfitting and improve generalization."
    elif "knn" in q:
        return "KNN can be good for small datasets but struggles with high dimensionality and noisy data."
    elif "features" in q or "important" in q:
        return "The most important features are glucose, BMI, and age — based on correlation and model importance scores."
    else:
        return "I'm still learning. Try asking about glucose, BMI, ROC-AUC, or which model is better."

# Chat interface
user_input = st.text_input("Ask a question:")

if user_input:
    response = get_bot_response(user_input)
    st.markdown(f"**🤖 Copilot:** {response}")
