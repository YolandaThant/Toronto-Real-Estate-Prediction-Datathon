"""
Exploratory Data Analysis for Cleaned Real Estate Data.
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    """
    Main method.
    """
    # Load data
    df = pd.read_csv("./cleaned_real_estate_data.csv")

    # 1. Look at the distribution of prices
    prices = df['price (In 1000s)']
    summary = prices.describe()

    # 2. Graph the distribution of prices
    # sns.set_style("white")
    # sns.set_context("notebook")
    # sns.histplot(prices, bins=40, stat="density", color="limegreen")
    # sns.kdeplot(prices, color="forestgreen", linewidth=1)
    # sns.despine()
    #
    # plt.xlabel("Price (in 1000s of Dollars)")
    # plt.title("Real Estate Prices")
    # plt.ylabel("Density")
    # plt.show()

    # 3. Compare Prices Across Wards
    sns.set_style("white")
    sns.set_context("notebook")
    sns.boxplot(data=df, x="ward", y="price (In 1000s)", width=0.5, fliersize=2, hue="ward", palette="rainbow", legend=False)
    sns.despine()

    plt.xticks(ticks=range(3), labels=["Toronto Centre", "Spadina-Fort York", "University-Rosedale"])
    plt.title("How Real Estate Prices Vary Across Neighborhoods")
    plt.xlabel("Ward (Neighborhood)")
    plt.ylabel("Price (in 1000s of Dollars")
    plt.show()


if __name__ == "__main__":
    main()
