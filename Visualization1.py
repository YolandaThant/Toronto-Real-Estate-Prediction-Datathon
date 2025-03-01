import pandas as pd

# Load dataset
dataset = pd.read_csv("Real Estate/real-estate-data.csv")

# Drop rows where 'size' is NA
dataset = dataset.dropna(subset=['size'])

# Check how many 'NA' values are in 'size' column: 53. 2989 rows
# na_size_count = dataset['size'].isna().sum()
# print(f"Number of rows with NA values in 'size' column: {na_size_count}")

# Convert empty strings in 'price' to NaN
dataset['price'] = dataset['price'].replace('', pd.NA)

# Check how many 'NA' values are in 'price' column: 61. 2928 rows
# na_price_count = dataset['price'].isna().sum()
# print(f"Number of rows with NA values in '[price]' column: {na_price_count}")

# Drop rows where 'price' is NaN (previously empty)
dataset = dataset.dropna(subset=['price'])

# Convert 'price' column to numeric (ensure no non-numeric values remain)
dataset['price'] = pd.to_numeric(dataset['price'])

# Remove 'sqft' from 'size' column
dataset['size'] = dataset['size'].str.replace(' sqft', '', regex=False)

# Convert empty strings in 'beds' to NaN
dataset['beds'] = dataset['beds'].replace('', pd.NA)

# Check how many 'NA' values are in 'beds' column: 50. 2878 rows
# na_beds_count = dataset['beds'].isna().sum()
# print(f"Number of rows with NA values in 'beds' column: {na_beds_count}")

# Drop rows where 'beds' is NaN
dataset = dataset.dropna(subset=['beds'])

# Function to clean and convert 'size' column
def convert_size(value):
    if '-' in value:  # If it's a range, calculate the median
        low, high = map(int, value.split('-'))
        return (low + high) // 2

# Apply function to 'size' column
dataset['size'] = dataset['size'].apply(convert_size)

# Rename 'price' column to 'price (In 1000s)'
dataset = dataset.rename(columns={'price': 'price (In 1000s)'})

# Convert 'price (In 1000s)' to thousands
dataset['price (In 1000s)'] = (dataset['price (In 1000s)'] / 1000).astype(int)

# Print the updated dataset
# print(dataset)

# (Optional) Save the cleaned dataset back to a CSV file
dataset.to_csv("cleaned_real_estate_data.csv", index=False)

