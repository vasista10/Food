import csv 
import pandas as pd 
import numpy as np 
from sklearn.naive_bayes import GaussianNB 
#pregnancy, Glucose, BP, SkinThickness, Insulin, BMI(Body mass Index), Diabetic, Age, Outcome 
data= pd.read_csv(r"C:\Users\shash\Downloads\p6.csv") 
x= np.array(data.iloc[:,0:-1]) 
y= np.array(data.iloc[:,-1]) 
print(data.head()) 
model= GaussianNB() 
 
model.fit(x,y) 
 
predicted = model.predict([[1,85,66,29,0,26.6,0.351,31]]) 
print("Predicted Value:",predicted) 