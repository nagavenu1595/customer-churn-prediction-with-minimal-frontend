import streamlit as st
import pandas as pd
import joblib
import json

# Load model and feature names
model = joblib.load("xgb_churn_model.pkl")
with open("xgb_features.json") as f:
    feature_names = json.load(f)

st.set_page_config(page_title="Churn Predictor", layout="centered")

st.title("🔍 Customer Churn Prediction App")
st.markdown("Enter customer information below:")

# Input form
with st.form("churn_form"):
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
    total = st.number_input("Total Charges", 0.0, 10000.0, 850.0)

    gender = st.selectbox("Gender", ["Female", "Male"])
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])
    phone = st.selectbox("Phone Service", ["Yes", "No"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No Internet"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Credit card (automatic)", "Bank transfer (automatic)"
    ])
    submit = st.form_submit_button("Predict")

if submit:
    input_dict = {
        'tenure': tenure,
        'MonthlyCharges': monthly,
        'TotalCharges': total,
        'gender_Male': 1 if gender == "Male" else 0,
        'SeniorCitizen': 1 if senior == "Yes" else 0,
        'Partner_Yes': 1 if partner == "Yes" else 0,
        'Dependents_Yes': 1 if dependents == "Yes" else 0,
        'PhoneService_Yes': 1 if phone == "Yes" else 0,
        'MultipleLines_Yes': 0,
        'MultipleLines_No phone service': 1 if phone == "No" else 0,
        'InternetService_Fiber optic': 1 if internet == "Fiber optic" else 0,
        'InternetService_No': 1 if internet == "No Internet" else 0,
        'OnlineSecurity_Yes': 0,
        'OnlineBackup_Yes': 0,
        'DeviceProtection_Yes': 0,
        'TechSupport_Yes': 0,
        'StreamingTV_Yes': 0,
        'StreamingMovies_Yes': 0,
        'Contract_One year': 1 if contract == "One year" else 0,
        'Contract_Two year': 1 if contract == "Two year" else 0,
        'PaperlessBilling_Yes': 1 if paperless == "Yes" else 0,
        'PaymentMethod_Electronic check': 1 if payment == "Electronic check" else 0,
        'PaymentMethod_Mailed check': 1 if payment == "Mailed check" else 0,
        'PaymentMethod_Credit card (automatic)': 1 if payment == "Credit card (automatic)" else 0,
    }

    # Fill missing values with 0
    for col in feature_names:
        if col not in input_dict:
            input_dict[col] = 0

    input_df = pd.DataFrame([input_dict])[feature_names]
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.markdown("## 🎯 Prediction Result")
    if prediction == 1:
        st.error(f"⚠️ Customer is likely to CHURN.")
    else:
        st.success(f"✅ Customer is NOT likely to churn.")

    st.metric("Churn Probability", f"{probability:.2%}")
