# Customer Churn Prediction using Machine Learning

## 📌 Project Overview

Customer churn refers to a customer stopping or discontinuing their service with a company.

This project uses Machine Learning to predict whether a customer is likely to **churn** based on information such as customer demographics, services used, contract type, tenure, monthly charges, and payment method.

The project uses **Logistic Regression** as the primary classification algorithm and provides a **Streamlit web application** for making predictions.

---

## 🎯 Objectives

- Understand customer churn data.
- Perform Exploratory Data Analysis (EDA).
- Clean and preprocess the dataset.
- Convert categorical data into numerical form.
- Train a Machine Learning classification model.
- Evaluate the model using classification metrics.
- Save the trained model using Joblib.
- Build a Streamlit application for customer churn prediction.

---

## 📂 Project Structure

```text
Customer_Churn_Prediction/
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── models/
│   ├── churn_model.pkl
│   └── other saved model files
│
├── notebooks/
│   └── customer_churn_analysis.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

**Dataset:** Telco Customer Churn

The dataset contains information about customers of a telecommunications company.

### Important Features

- `customerID` – Unique customer identifier
- `gender` – Customer gender
- `SeniorCitizen` – Whether the customer is a senior citizen
- `Partner` – Whether the customer has a partner
- `Dependents` – Whether the customer has dependents
- `tenure` – Number of months the customer has stayed with the company
- `PhoneService` – Whether phone service is subscribed
- `InternetService` – Type of internet service
- `Contract` – Customer contract type
- `PaymentMethod` – Customer payment method
- `MonthlyCharges` – Monthly amount charged
- `TotalCharges` – Total amount charged
- `Churn` – Whether the customer left the company

### Target Variable

```text
Churn
```

The target contains two classes:

```text
Yes → Customer churned
No  → Customer did not churn
```

---

## 🔧 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

---

## 🧹 Data Preprocessing

The following preprocessing steps are performed:

1. Load the dataset.
2. Check the dataset structure.
3. Check missing values.
4. Check duplicate records.
5. Remove unnecessary columns.
6. Handle missing values.
7. Convert categorical variables into numerical variables.
8. Separate features and target variable.
9. Split the dataset into training and testing sets.
10. Apply feature scaling where required.

---

## 📈 Exploratory Data Analysis

EDA is performed to understand relationships and patterns in the dataset.

Some visualizations include:

- Churn distribution
- Churn by contract type
- Churn by internet service
- Churn by gender
- Churn based on tenure
- Monthly charges distribution
- Correlation analysis

---

## 🤖 Machine Learning Model

### Logistic Regression

Logistic Regression is used because this is a **binary classification problem**.

The model predicts:

```text
0 → No Churn
1 → Churn
```

---

## 📏 Model Evaluation

The trained model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Example:

```text
Accuracy  : XX%
Precision : XX%
Recall    : XX%
F1-Score  : XX%
```

> The actual values will be updated after training the model.

---

## 💾 Model Saving

The trained Machine Learning model is saved using Joblib.

Example:

```python
import joblib

joblib.dump(model, "models/churn_model.pkl")
```

The saved model can later be loaded by the Streamlit application.

---

## 🌐 Streamlit Application

A Streamlit web application is created to allow users to enter customer information and receive a churn prediction.

### Application Flow

```text
Customer Details
       ↓
Data Preprocessing
       ↓
Trained ML Model
       ↓
Prediction
       ↓
Churn / No Churn
```

The application provides an easy-to-use interface for customer churn prediction.

---

## ▶️ How to Run the Project

### 1. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib streamlit
```

### 2. Run the Streamlit Application

Open the project folder in the terminal and run:

```bash
python -m streamlit run app.py
```

The application will open in the browser.

---

## 🔮 Future Improvements

- Compare Logistic Regression with Random Forest, Decision Tree, KNN, and XGBoost.
- Perform hyperparameter tuning.
- Improve model performance.
- Add probability of churn.
- Add more interactive Streamlit visualizations.
- Deploy the application online.
- Add customer retention recommendations.

---

## 👩‍💻 Author

**Harshitha Nunna**

B.Tech – Computer Science and Engineering

---

## 📌 Conclusion

This project demonstrates an end-to-end Machine Learning workflow, starting from **data collection and EDA** through **data preprocessing, model training, evaluation, model saving, and deployment using Streamlit**.

The system can help businesses identify customers who are more likely to churn and potentially take preventive customer-retention actions.