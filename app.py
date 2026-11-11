import streamlit as st
import pandas as pd
import joblib

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# LOAD MODEL AND PREPROCESSOR
# =========================================================

model = joblib.load("models/churn_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

# =========================================================
# HEADER
# =========================================================

st.title("📊 Customer Churn Prediction System")

st.write(
    "An industry-oriented Machine Learning application "
    "for predicting telecom customer churn."
)

st.divider()

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.header("📌 Project Information")

st.sidebar.write(
    """
    **Machine Learning Model:**  
    Random Forest

    **Application:**  
    Customer Churn Prediction

    **Target:**  
    Customer Churn

    **Deployment:**  
    Streamlit
    """
)

st.sidebar.divider()

st.sidebar.subheader("📈 Business Objective")

st.sidebar.write(
    "Identify customers who are likely to leave "
    "the telecom service so that retention strategies "
    "can be applied."
)

# =========================================================
# CUSTOMER INFORMATION
# =========================================================

st.subheader("👤 Customer Information")

col1, col2, col3 = st.columns(3)

# ---------------------------------------------------------
# COLUMN 1
# ---------------------------------------------------------

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=100,
        value=12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        [
            "Yes",
            "No",
            "No phone service"
        ]
    )

# ---------------------------------------------------------
# COLUMN 2
# ---------------------------------------------------------

with col2:

    internet_service = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

    online_security = st.selectbox(
        "Online Security",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    online_backup = st.selectbox(
        "Online Backup",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    device_protection = st.selectbox(
        "Device Protection",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    tech_support = st.selectbox(
        "Tech Support",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

# ---------------------------------------------------------
# COLUMN 3
# ---------------------------------------------------------

with col3:

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=1000.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=100000.0,
        value=1000.0
    )

st.divider()

# =========================================================
# CREATE INPUT DATAFRAME
# =========================================================

input_data = pd.DataFrame({

    "gender": [gender],

    "SeniorCitizen": [senior_citizen],

    "Partner": [partner],

    "Dependents": [dependents],

    "tenure": [tenure],

    "PhoneService": [phone_service],

    "MultipleLines": [multiple_lines],

    "InternetService": [internet_service],

    "OnlineSecurity": [online_security],

    "OnlineBackup": [online_backup],

    "DeviceProtection": [device_protection],

    "TechSupport": [tech_support],

    "StreamingTV": [streaming_tv],

    "StreamingMovies": [streaming_movies],

    "Contract": [contract],

    "PaperlessBilling": [paperless_billing],

    "PaymentMethod": [payment_method],

    "MonthlyCharges": [monthly_charges],

    "TotalCharges": [total_charges]
})

# =========================================================
# PREDICTION
# =========================================================

if st.button(
    "🔮 Predict Customer Churn",
    use_container_width=True
):

    # Transform input
    input_processed = preprocessor.transform(input_data)

    # Prediction
    prediction = model.predict(input_processed)[0]

    # Probability
    probability = model.predict_proba(
        input_processed
    )[0][1]

    churn_percentage = probability * 100

    st.divider()

    st.subheader("📋 Prediction Result")

    # =====================================================
    # RESULT
    # =====================================================

    if prediction == 1:

        st.error(
            "⚠️ HIGH RISK: Customer is likely to churn"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Churn Probability",
                f"{churn_percentage:.2f}%"
            )

        with col2:
            st.metric(
                "Prediction",
                "CHURN"
            )

        st.warning(
            """
            **Business Recommendation**

            • Offer a personalized retention discount  
            • Consider contract upgrade incentives  
            • Contact the customer proactively  
            • Provide additional technical support  
            • Analyze dissatisfaction factors
            """
        )

    else:

        st.success(
            "✅ LOW RISK: Customer is likely to stay"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Churn Probability",
                f"{churn_percentage:.2f}%"
            )

        with col2:
            st.metric(
                "Prediction",
                "NO CHURN"
            )

        st.info(
            """
            **Business Recommendation**

            • Continue good customer service  
            • Maintain customer engagement  
            • Offer loyalty benefits  
            • Monitor future customer behavior
            """
        )

    # =====================================================
    # PROBABILITY BAR
    # =====================================================

    st.subheader("📊 Churn Risk Level")

    st.progress(
        min(int(churn_percentage), 100)
    )

    if churn_percentage >= 70:

        st.error(
            "🔴 High Churn Risk"
        )

    elif churn_percentage >= 40:

        st.warning(
            "🟡 Medium Churn Risk"
        )

    else:

        st.success(
            "🟢 Low Churn Risk"
        )

    # =====================================================
    # INPUT SUMMARY
    # =====================================================

    st.subheader("📝 Customer Input Summary")

    summary = pd.DataFrame({
        "Feature": input_data.columns,
        "Value": input_data.iloc[0].values
    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Customer Churn Prediction System | "
    "Machine Learning + Random Forest + Streamlit"
)