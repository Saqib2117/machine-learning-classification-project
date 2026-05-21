# Adult Income Prediction System

## Project Overview
The Adult Income Prediction System is a Machine Learning web application developed using Streamlit. The project predicts whether a person's annual income is less than or equal to 50K (`<=50K`) or greater than 50K (`>50K`) based on demographic and work-related information.

---

## Technologies Used
- NumPy
- Pandas
- Scikit-learn
- Imbalanced-learn (Imblearn)
- Matplotlib
- Seaborn
- FastAPI
- Streamlit

---

## Accuracy of All Models
The following machine learning models were trained and evaluated:

| Model | Accuracy |
|---|---|
| Logistic Regression | 79.44% |
| Decision Tree Classifier | 81.03% |
| Support Vector Classifier (SVC) | 80.1% |
| K-Nearest Neighbors (K-NN) | 78.07% |

---

## Best Performing Model
The best-performing model based on accuracy is the Decision Tree Classifier with an accuracy of 81.03%. Therefore, this model was selected and saved for income prediction.

---

## Backend Deployment
The backend API was developed using FastAPI with a `/predict` route. The backend model API was deployed on Hugging Face.

---

## Streamlit Deployment
The frontend was developed using Streamlit and connected with the FastAPI backend to predict a user's income category based on the provided information.

### Streamlit Deployed Link
https://ml-income-classifier.streamlit.app/