# 🔍 Customer Churn Prediction App

This is an interactive web app built with **Streamlit** that predicts whether a customer is likely to churn based on their details. It uses a trained **XGBoost classifier** and allows users to input customer data through a user-friendly interface.

---

## 🧠 Features

- Input customer details using dropdowns and sliders
- Real-time churn prediction using a trained model
- Displays churn probability with a friendly UI
- minimal Custom styling using HTML/CSS inside Streamlit

---

## 🛠️ Tech Stack

- **Streamlit** for the frontend
- **XGBoost** for the machine learning model
- **Scikit-learn & Pandas** for preprocessing
- **Joblib** to load the trained model

---

## requirements to download
- streamlit
- xgboost
- scikit-learn
- pandas
- numpy
- joblib


## 📁 Files Included

| File                      | Description                                 |
|---------------------------|---------------------------------------------|
| `app.py`                 | Main Streamlit app                          |
| `xgb_churn_model.pkl`    | Trained XGBoost model                       |
| `xgb_features.json`      | List of features used during training       |
| `churn.csv`              | Dataset (for reference)                     |
| `ccp.ipynb`              | Notebook used for model building            |

---

## ⚙️ Setup Instructions (Run Locally)

1. Clone the repo:
   ```bash
   git clone https://github.com/nagavenu1595/customer-churn-prediction-with-minimal-frontend.git
   cd customer-churn-prediction-with-minimal-frontend
