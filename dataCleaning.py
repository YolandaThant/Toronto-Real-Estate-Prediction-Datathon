import pandas as pd

# Load dataset
dataset = pd.read_csv("Real Estate/real-estate-data.csv")

# Drop rows where 'size' is NA
dataset = dataset.dropna(subset=['size'])

# Convert empty strings in 'price' to NaN
dataset['price'] = dataset['price'].replace('', pd.NA)

# Drop rows where 'price' is NaN
dataset = dataset.dropna(subset=['price'])

# Convert 'price' column to numeric (ensure no non-numeric values remain)
dataset['price'] = pd.to_numeric(dataset['price'])

# Remove 'sqft' from 'size' column
dataset['size'] = dataset['size'].str.replace(' sqft', '', regex=False)

# Convert empty strings in 'beds' to NaN
dataset['beds'] = dataset['beds'].replace('', pd.NA)

# Drop rows where 'beds' is NaN
dataset = dataset.dropna(subset=['beds'])

# Function to clean and convert 'size' column
def convert_size(value):
    if '-' in value:  # If it's a range, calculate the median
        low, high = map(int, value.split('-'))
        return ((low + high) // 2) + 1
    elif value.isdigit():  # If it's a single number, return it as an integer
        return int(value)
    else:
        return None  # Handle unexpected cases (optional)

# Apply function to 'size' column
dataset['size'] = dataset['size'].apply(convert_size)

# Drop NaN values in 'size' if any exist
dataset = dataset.dropna(subset=['size'])

# Rename 'price' column to 'price (In 1000s)'
dataset = dataset.rename(columns={'price': 'price (In 1000s)'})

# Convert 'price (In 1000s)' to thousands
dataset['price (In 1000s)'] = (dataset['price (In 1000s)'] / 1000).astype(int)

# (Optional) Save the cleaned dataset back to a CSV file
dataset.to_csv("cleaned_real_estate_data.csv", index=False)

# Check summary of cleaned data
# print(dataset['size'].head())
