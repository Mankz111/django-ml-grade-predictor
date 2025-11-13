import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import mean_absolute_error,r2_score
import joblib
import os


data = pd.read_csv("Student_Grades.csv")
X = data.drop("Grade",axis=1)
grade_map = {"A" : 4, "B" : 3, "C": 2, "D": 1, "F": 0}
y = data["Grade"].map(grade_map)

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42, test_size=0.2)
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

model_filename = 'train_model.joblib'
model_path = os.path.join(os.path.dirname(__file__), model_filename)
joblib.dump(model, model_path)