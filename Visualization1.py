import pandas as pd

# Load dataset
dataset = pd.read_csv("Real Estate/real-estate-data.csv")

# Drop rows where 'size' is NA
dataset = dataset.dropna(subset=['size'])

# Remove 'sqft' from 'size' column
dataset['size'] = dataset['size'].str.replace(' sqft', '', regex=False)

# Function to clean and convert 'size' column
def convert_size(value):
    if '-' in value:  # If it's a range, calculate the median
        low, high = map(int, value.split('-'))
        return (low + high) // 2
    elif '+' in value:  # If there's a '+' sign, remove it and use the base value
        return int(value.replace('+', ''))
    else:  # If it's a single number, convert directly
        return int(value)

# Apply function to 'size' column
dataset['size'] = dataset['size'].apply(convert_size)

# Print the entire updated dataset
# print(dataset)

# (Optional) Save the cleaned dataset back to a CSV file
dataset.to_csv("cleaned_real_estate_data.csv", index=False)

