import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('loan_approval_model.pkl')

# Streamlit app header
st.header('Loan Prediction')

# Input fields for the user to provide data
gender = st.selectbox('Gender', ['Male', 'Female'])
married = st.selectbox('Married?', ['Yes', 'No'])
dependents = st.slider('Number of Dependents', 0, 3)
education = st.selectbox('Education Level', ['Graduate', 'Not Graduate'])
self_employed = st.selectbox('Self-Employed?', ['Yes', 'No'])
applicant_income = st.number_input('Applicant Income', 0, 1000000)
coapplicant_income = st.number_input('Coapplicant Income', 0, 1000000)
loan_amount = st.number_input('Loan Amount', 0, 1000000)
loan_amount_term = st.slider('Loan Amount Term (in months)', 0, 480)
credit_history = st.selectbox('Credit History', ['Good History', 'Bad History' , 'No History'])  # Changed to selectbox
property_area = st.selectbox('Property Area', ['Urban', 'Semiurban', 'Rural'])

# Converting categorical variables into numerical form for prediction
if gender == 'Male':
    gender = 1
else:
    gender = 0

if married == 'Yes':
    married = 1
else:
    married = 0

if education == 'Graduate':
    education = 0
else:
    education = 1

if self_employed == 'Yes':
    self_employed = 1
else:
    self_employed = 0

if credit_history == 'Good History':
    credit_history = 1
else:
    credit_history = 0

if property_area == 'Urban':
    property_area = 2
elif property_area == 'Semiurban':
    property_area = 1
else:
    property_area = 0

# Predict the loan status
if st.button("Predict Loan Approval"):
    input_data = pd.DataFrame([[gender, married, dependents, education, self_employed,
                                applicant_income, coapplicant_income, loan_amount, loan_amount_term,
                                credit_history, property_area]],
                              columns=['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 
                                       'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 
                                       'Credit_History', 'Property_Area'])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.markdown('Loan is **Approved**')
    else:
        st.markdown('Loan is **Rejected**')

