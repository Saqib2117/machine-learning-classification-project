import streamlit as st
import requests

BASE_URL = "https://saqib21-fastapi-backend.hf.space"

st.set_page_config(page_title="Income Level Prediction", page_icon=r"C:\Users\Saqib\Documents\ML Assignement\Machine Learning Project\frontend\income.png")
st.title("Machine Learning Model for Income Level Prediction")
st.write("Enter the following details to predict the income level:")

education_map = {
    "11th Grade": 7,
    "High School Graduate": 9,
    "Associate Academic Degree": 12,
    "Some College (No Degree)": 10,
    "10th Grade": 6,
    "Professional School": 15,
    "7th-8th Grade": 4,
    "Bachelor's Degree": 13,
    "Master's Degree": 14,
    "Doctorate / PhD": 16,
    "5th-6th Grade": 3,
    "Associate Vocational Degree": 11,
    "9th Grade": 5,
    "12th Grade": 8,
    "1st-4th Grade": 2,
    "Preschool": 1
}

region_options = ['United-States', 'Peru', 'Guatemala', 'Mexico',
       'Dominican-Republic', 'Ireland', 'Germany', 'Philippines',
       'Thailand', 'Haiti', 'El-Salvador', 'Puerto-Rico', 'Vietnam',
       'South', 'Columbia', 'Japan', 'India', 'Cambodia', 'Poland',
       'Laos', 'England', 'Cuba', 'Taiwan', 'Italy', 'Canada', 'Portugal',
       'China', 'Nicaragua', 'Honduras', 'Iran', 'Scotland', 'Jamaica',
       'Ecuador', 'Yugoslavia', 'Hungary', 'Hong', 'Greece',
       'Trinadad&Tobago', 'Outlying-US(Guam-USVI-etc)', 'France',
       'Holand-Netherlands'
]

age = st.number_input("Age", min_value=0, max_value=100, value=30)
workclass = st.selectbox("Workclass", ["Private", 'Government', 'Other'])
education = st.selectbox("Education", list(education_map.keys()))
marital_status = st.selectbox("Marital Status", ['Single', 'Married', 'Previously-Married'])
occupation = st.selectbox("Occupation", ["Low-Skill", "Mid-Skill", "High-Skill"])
relationship = st.selectbox("Relationship", ['Own-child', 'Husband', 'Not-in-family', 'Unmarried', 'Wife', 'Other-relative'])
gender = st.selectbox("Gender", ['Male', 'Female'])
hours_per_week = st.number_input("Hours per week", min_value=0, max_value=168, value=40)
native_country = st.selectbox("Native Country", region_options)
capital_total = st.number_input("Capital Total", min_value=0, value=0)

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
