import os
import joblib
import numpy as np
from sklearn.model_selection import train_test_split

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'train_model.joblib')


try:
    MODEL = joblib.load(MODEL_PATH)
except FileNotFoundError:
    raise(f'The as not found in this {MODEL_PATH}')

def predictor(input1,input2):
    features = np.np.array([[input1,input2]])
    MODEL.predict(features)[0]
    


