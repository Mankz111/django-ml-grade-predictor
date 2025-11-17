import os
import joblib
import numpy as np
from sklearn.model_selection import train_test_split

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'train_model.joblib')


try:
    MODEL = joblib.load(MODEL_PATH)
except FileNotFoundError:
    raise(f'The as not found in this {MODEL_PATH}')

def predictor(hours,practice, teamwork, midterm, finalexam, scores):
    features = np.array([[hours,practice, teamwork, midterm, finalexam, scores]])
    predicted_value = MODEL.predict(features)[0]
    grades = {4 : "A", 3 : "B", 2 : "C", 1 : "D", 0 : "F"}
    rounded_grade = round(predicted_value)
    predicted_grade = grades.get(rounded_grade, 'Error')
    return predicted_grade

    





    


