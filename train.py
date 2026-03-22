import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
import joblib

df = pd.read_csv("house.csv")
df.head()

df.tail()

x = df[['area']]
y = df[['price']]
x_train,x_test,y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 42)

model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

r2 = r2_score(y_test,y_pred)
mse = mean_squared_error(y_test,y_pred)

r2

mse

df["Area_predict"] = model.predict(x)

plt.scatter(x,y,color = "blue", label = "Actual Data")
plt.plot(x,df['Area_predict'], color = 'red', label = "Regression Line")
plt.xlabel("area")
plt.ylabel("price")
plt.title("Linear Regression(House): Area Vs Price")
plt.legend()
plt.show()

# Save the trained model
joblib.dump(model, 'model.pkl')

# Load the trained model (for testing purposes)
loaded_model = joblib.load('model.pkl')