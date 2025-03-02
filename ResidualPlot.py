import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

# Read the data from the dataset
data = pd.read_csv("cleaned_real_estate_data.csv")

# Drop rows w/ NA values in 'size' or 'price' columns
df = data.dropna(subset=['size', 'price (In 1000s)'])

# Define independent & dependent variables
x = df['size'].values.reshape(-1, 1)
y = df['price (In 1000s)']

# Fitting the Linear Regression model
model = LinearRegression()
model.fit(x, y)

# Linear Regression Equation
slope = model.coef_[0]
intercept = model.intercept_
print(f"Linear Regression Equation: Price = {slope:.2f} * Square_Feet + {intercept:.2f}")

# Predict prices (values for y) using the model
y_hat = model.predict(x)

# Compute residuals (difference b/w actual & predicted values)
residuals = y - y_hat

# Plotting the residuals
plt.figure(figsize=(8, 5))
plt.scatter(y_hat, residuals, color='limegreen', alpha=0.2)
plt.axhline(y=0, color='red', linestyle='--', linewidth=2)
plt.xlabel("Predicted Price (In Thousands CAD) in y_hat")
plt.ylabel("Residual in (y - y_hat)")
plt.title("Residual Plot of Prediction vs Housing Prices (In Thousands CAD)")

plt.show()
