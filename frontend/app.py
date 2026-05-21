import streamlit as st
import requests

BASE_URL = "https://saqib21-fastapi-backend.hf.space"

st.set_page_config(page_title="Income Level Prediction", page_icon="💰")
st.title("Machine Learning Model for Income Level Prediction")
st.write("Enter the following details to predict the income level:")

age = st.number_input("Age", min_value=0, max_value=100, value=30)
workclass = st.selectbox("Workclass", ["Private", 'Government', 'Other'])
education = st.selectbox("Education", ['11th', 'HS-grad', 'Assoc-acdm', 'Some-college', '10th',
       'Prof-school', '7th-8th', 'Bachelors', 'Masters', 'Doctorate',
       '5th-6th', 'Assoc-voc', '9th', '12th', '1st-4th', 'Preschool'])
marital_status = st.selectbox("Marital Status", ['Single', 'Married', 'Previously-Married'])
occupation = st.selectbox("Occupation", ["Low-Skill", "Mid-Skill", "High-Skill"])
relationship = st.selectbox("Relationship", ['Own-child', 'Husband', 'Not-in-family', 'Unmarried', 'Wife', 'Other-relative'])
gender = st.selectbox("Gender", ['Male', 'Female'])
hours_per_week = st.number_input("Hours per week", min_value=0, max_value=168, value=40)
native_country = st.selectbox("Native Country", ['United-States', 'Peru', 'Guatemala', 'Mexico',
       'Dominican-Republic', 'Ireland', 'Germany', 'Philippines',
       'Thailand', 'Haiti', 'El-Salvador', 'Puerto-Rico', 'Vietnam',
       'South', 'Columbia', 'Japan', 'India', 'Cambodia', 'Poland',
       'Laos', 'England', 'Cuba', 'Taiwan', 'Italy', 'Canada', 'Portugal',
       'China', 'Nicaragua', 'Honduras', 'Iran', 'Scotland', 'Jamaica',
       'Ecuador', 'Yugoslavia', 'Hungary', 'Hong', 'Greece',
       'Trinadad&Tobago', 'Outlying-US(Guam-USVI-etc)', 'France',
       'Holand-Netherlands'])
capital_total = st.number_input("Capital Total", min_value=0, value=0)

education_map = {
    'Preschool': 1,
    '1st-4th': 2,
    '5th-6th': 3,
    '7th-8th': 4,
    '9th': 5,
    '10th': 6,
    '11th': 7,
    '12th': 8,
    'HS-grad': 9,
    'Some-college': 10,
    'Assoc-voc': 11,
    'Assoc-acdm': 12,
    'Bachelors': 13,
    'Masters': 14,
    'Prof-school': 15,
    'Doctorate': 16
}

education_num = education_map[education]

if st.button("Predict"):

    data = {
        "age": age,
        "workclass": workclass,
        "educational_num": education_num,
        "marital_status": marital_status,
        "occupation": occupation,
        "relationship": relationship,
        "gender": gender,
        "hours_per_week": hours_per_week,
        "native_country": native_country,
        "capital_total": capital_total
    }

    response = requests.post(f"{BASE_URL}/predict", params=data)

    if response.status_code == 200:
        result = response.json()
        if result.get("prediction"):
            st.success(result.get("prediction"))
        else:
            st.error("Oops! Prediction failed. Please try again.")
    else:
        st.error("Error: Unable to get a response from the server. Please try again later.")
