"""
Exploratory Data Analysis for Cleaned Real Estate Data.
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    # Load data
    df = pd.read_csv("./cleaned_real_estate_data.csv")
    
    # 1. Look at the distribution of prices
    prices = df['price (In 1000s)']
    summary = prices.describe()
    print(summary["75%"] - summary["25%"])


if __name__ == "__main__":
    main()