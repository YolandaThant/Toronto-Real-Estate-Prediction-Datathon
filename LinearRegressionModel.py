import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


# read the data from the dataset
data = pd.read_csv("cleaned_real_estate_data.csv")

df = data.dropna(subset=['size'])

x = df[['size']]
y = df['price (In 1000s)']



model = LinearRegression()
model.fit(x,y)

slope = model.coef_[0]
intercept = model.intercept_

print(f"Linear Regression Equation: Price = {slope:.2f} * Square_Feet + {intercept:.2f}")

