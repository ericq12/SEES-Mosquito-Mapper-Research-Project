import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics


df = pd.read_csv(r'C:\Users\ericq\Downloads\test.csv')
# Replace 'C:\Users\ericq\Downloads\test.csv' with file path of downloaded CSV

X = df[['Elevation (m)', 'Soil Moisture']].values
y = df['Larvae Count'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = LinearRegression()  
regressor.fit(X_train, y_train)

print(regressor.intercept_)
print(regressor.coef_)

y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
sample = df.head(25)
print(sample)
