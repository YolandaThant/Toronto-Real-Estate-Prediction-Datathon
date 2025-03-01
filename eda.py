"""
Exploratory Data Analysis for Cleaned Real Estate Data.
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math


def main():
    """
    Main method.
    """
    # Load data
    df = pd.read_csv("./cleaned_real_estate_data.csv")

    # 1. Look at the distribution of prices
    prices = df['price (In 1000s)']
    summary = prices.describe()
    print(summary["75%"] - summary["25%"])

    # 2. Graph the distribution of prices
    sns.set_style("white")
    sns.set_context("notebook")
    sns.histplot(prices, bins=40, stat="density", color="limegreen")
    sns.kdeplot(prices, color="forestgreen", linewidth=1)
    sns.despine()

    plt.xlabel("Price (in 1000s of Dollars)")
    plt.ylabel("Density")
    plt.show()


if __name__ == "__main__":
    main()
