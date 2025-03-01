import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.linear_model import LinearRegression

# read the data from the dataset
data = pd.read_csv("cleaned_real_estate_data.csv")

# make it into a dataframe
df = pd.DataFrame(data)

x = df[['size']]
y = df['price (In 1000s)']

model = LinearRegression()
model.fit(x,y)

slope = model.coef_[0]
intercept = model.intercept_


print(f"Linear Regression Equation: Price = {slope:.2f} * Square_Feet + {intercept:.2f}")
