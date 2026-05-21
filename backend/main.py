from fastapi import FastAPI
import pickle as pkl
import pandas as pd

app = FastAPI()

def load_model():
    with open('model.pkl', 'rb') as f:
        model = pkl.load(f)
    return model

@app.get("/")
def home():
    return {"message": "Welcome to Machine Learning API!"}

@app.post('/predict')
def predict(age: int, workclass: str, educational_num: int, marital_status: str, occupation: str, relationship: str, gender: str, hours_per_week: int, native_country: str, capital_total: int):
    model = load_model()

    data = pd.DataFrame({
        'age': [age],
        'workclass': [workclass],
        'educational_num': [educational_num],
        'marital_status': [marital_status],
        'occupation': [occupation],
        'relationship': [relationship],
        'gender': [gender],
        'hours_per_week': [hours_per_week],
        'native_country': [native_country],
        'capital_total': [capital_total]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        result = "Predicted income is greater than 50K"
    else:
        result = "Predicted income is less than or equal to 50K"
    return {"prediction": result}