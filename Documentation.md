# SDSS Datathon 2025
## Table of Contents 📚
1. [Introduction](#1-introduction-)
2. [Dataset](#2-our-dataset-)
3. [Initial Findings](#3-exploratory-data-analysis-and-initial-findings-)
4. [Visualizations](#4-visualizations-)
5. [Our Model](#5-our-model-)
7. [Results](#6-results-)
6. [Discussion](#7-discussion-)

## 1. Introduction 💡
Real estate markets are constantly evolving, and are an interest of potential homeowners, investors, real-estate agents, and city planners. Property values are influenced by a variety of factors and grasping their relative importance is key to understanding future pricing trends. However, the market’s complexity can present significant challenges in making accurate predictions. Developing a reliable prediction model is essential for understanding these trends, enabling better decision-making for relevant parties.

In this project, we take a look at recent real estate trends in the city of Toronto. In considering the relationships between real estate prices and factors like location, amenities, etc. we seek to inform future predictions about the quality and pricing of housing in downtown Toronto. This information could contribute to more informed investment, home buying, selling, and city planning. The information uncovered in this investigation could also be relevant in highlighting discrepancies between housing prices and income in Toronto, thus informing the need for more affordable housing or rent control.

## 2. Our Dataset 👩‍💻
### 2.1 Description
This dataset is a simulated representation of the Toronto real estate market, designed to reflect condo sales prices listed on the Multiple Listing Service. It focuses specifically on Toronto’s downtown core, covering three wards as defined by the City of Toronto (Wards 10, 11, and 13). The data have been curated to closely resemble real-world trends and variable relationships, enabling meaningful analysis. Please see [here](https://drive.google.com/drive/u/0/folders/1Y1sOZAPeHhqiO_hwkCkz_H6BPT-WXZEU) for more information.

#### 2.1.1 Relevant Fields
* **id**: A unique 6-digit identifier for each building.
* **ward**: The ward number the building is located in.
    * W10 - Spadina-Fort York
    * W11 - University-Rosedale
    * W13 - Toronto Centre
* **beds**: The number of bedrooms units in the building have.
* **baths**: The number of bathrooms units in the building have.
* **size**: The range of square footage units in the building with the given number of beds and baths have.
* **building age**: The age (in years) of the building.
* **price**: The listing [purchase] price of a unit in the building in CAD.

### 2.2 License
This dataset was provided by the *Students in Data Science and Statistics* and is licensed under City of Toronto's Open Government License. For more information on license information, please visit City of Toronto's [website](https://www.toronto.ca/city-government/data-research-maps/open-data/open-data-licence/).

### 2.3 Preprocessing Steps
1. In our analysis, the most important factor we are considering is the **size** (square footage) of building units. We therefore removed all entries where size was *NA*.
2. Size was given in ranges of 500 square feet and as string values. We took the median value for each range and converted to integers.
    * **e.g. "1500-1999 sqft" becomes 1750.**
3. Some entries did not have prices provided. We removed those entries.
4. Of the entries that did provide prices, we divided all values by 1000 to increase readability.

After processing, we were left with 2870 entries.

### 2.4 Justification
Our dataset has 3042 entries of different residential buildings across three wards in Toronto (Spadina-Fort York, University-Rosedale, and Toronto Centre). Each entry includes information about building amenities, location, age, and price. The dataset can thus be used to examine how price varies according to such factors. Further study can be conducted by cross-referncing each building with more information about its ward's demographic, which can be found [here](https://www.toronto.ca/city-government/data-research-maps/neighbourhoods-communities/ward-profiles/).

## 3. Exploratory Data Analysis and Initial Findings 🔍
Ultimately, we are interested in studying the prices of real estate units across Toronto. Let's take a look at the price distribution of buildings in our data set.

We can use Python to compute some quick summary statistics:
```
# Load data
df = pd.read_csv("./cleaned_real_estate_data.csv")

# Summarize data 
prices = df['price (In 1000s)']
summary = prices.describe()
print(summary)

>>> count    2928.000000
>>> mean      894.598702
>>> std       560.099359
>>> min       298.000000
>>> 25%       551.000000
>>> 50%       717.500000
>>> 75%      1012.250000
>>> max      5688.000000
```
From this information, it seems the average property has a list price of $894k. However, it is important to observe that the range of our data is $5,390k. This is an *incredible* amount of variation, especially with regards to the IQR of $461.25k. Looking at our minimum and maximum values, it seems like our data may be right-skewed. To confirm this, we have to take a look at the distribution graphically.

<figure>
    <img src="./price_density.png"/>
    <figcaption><strong>Fig. 1:</strong> Density histogram of price (in thousands of CAD).</figcaption>
</figure>

From this figure, we confirm that the price distribution is right-skewed. Moreover, we see that the majority of real estate properties have a price that falls within the range of $250,000 - $1,000,000. From this information, we can conclude that our previous sample mean may not be robust enough to reflect the actual mean property value.

We had previously obtained a median list price of $717k. Comparing this to the [2024's Q4 average condo sale price](https://trreb.ca/market-data/condo-market-report/) in Toronto, $689,198, we see that our median is a much closer approximation to this.

For some extra investigation, let's see if the distribution of prices varies across the 3 neighborhoods (wards) we examine.

<figure>
    <img src="./ward_vs_price.png"/>
    <figcaption><strong>Fig. 2:</strong> Ward vs. price (in 1000s of CAD)</figcaption>
</figure>

It seems that real estate prices are distributed similarly across the three wards. University-Rosedale (on average) has the most expensive units, while Spadina-Fort York encompasses the unit with the highest list price. But overall, there is little discernable difference between them.

## 4. Visualizations 📊
For the visualization of the price against the size of an aprtment, we decided to use a joint plot to clearly see the relationship between the two variables while also seeing the marginal distributions. The joint plot is displayed below: 
<figure>
    <img src="./joint_plot.png"/>
    <figcaption><strong>Fig. 3:</strong> Size vs. price (in 1000s of CAD)</figcaption>
</figure>
The joint plot shows a positive linear correlation between the size of the house and the price which makes sense as the price is likely to be higher for a bigger house. It can be seen through the figure that as the size of the apartment increases, the data points seem to gradually grow apart suggesting that for apartments that are bigger in size, the prices are more variable compared to smaller apartments whose prices are more similar. A possible analysis for the variable prices could be due to the neighbourhood that the apartments are in or the amenities provided. 
The marginal distribution also provide insights into the individual variables. The sizes of the houses show a right skewed distributions suggesting that many of the houses have smaller sizes with an average of 589 square feet, this would mean that most the apartments are within the range of 500-999 which is accurate as Toronto mostly has skyscrappers thereby the explaining the right skewed distribution.

To visualize the price versus the number of bedrooms in a unit, we utilized a box plot to effectively compare price distributionds across different unit types. The box plot allows us to clearly observe the spread of prices, detect outliers, and identify trends in price variability across bedroom categories. By using this visualization, we can see how price distributions differ between 0, 1, 2, and 3-bedroom apartments while also highlighting the presence of extreme values. The box plot is displayed below:
<figure>
    <img src="./prices_vs_room.png"/>
    <figcaption><strong>Fig. 4:</strong> Rooms vs. price (in 1000s of CAD)</figcaption>
</figure>
As expected, apartments with more bedrooms generally have higher prices, but the spread of prices also increases with the number of bedrooms. The variability in prices is particularly notable for two and three-bedroom apartments. This suggests a wider range of factors influencing pricing, such as location, amenities, or unit size. One-bedroom and studio apartments exhibit a more compact price distribution, indicating that prices for smaller units tend to be more consistent. The presence of outliers, especially for larger apartments, highlights high-end listings that significantly exceed the typical price range. The right-skewed distribution aligns with market trends in Toronto, where luxury units and penthouses drive up the upper end of the pricing spectrum.

## 5. Our Model ⚡️
In order to be able to predict the values, we decicded to use the linear regression model. The linear regression model we found is:  price = 0.80 * size + 208.81. 
This suggests that for every square foot of size, the price increases by CAD 800. The R^2 error is given as 0.77 suggesting that 77% of the price variance can be explained by the size of the house. 

<figure>
    <img src="./residual_plot.png"/>
    <figcaption><strong>Fig. 1:</strong> Residual Plot for Prediction vs Housing Prices (In Thousands CAD).</figcaption>
</figure>
From the underlying residual plot, although the variance (vertical spread) increases as the fitted values (predicted values) increase, there appears to be no convex or concave curve shape in this plot. This indicates the points are (sort of) randomly spread out, and that a linear regression model does a good job of fitting the data.
With that being said, a possible reason to why the variance (vertical spread) increases is because of the way **the dataset was given to us**: size of housing was in intervals. Thus, we decided to pick a size from the interval, which is by the median of each interval.

## 6. Results ❗️
We also split the dataset into 80% training data and 20% testing data to see check if the model predicts the prices correctly. However becasue we have divided our size as the median of the different intervals, the prices for a particular size is variable resulting in large differences betweent he actual and predicted values and in fact this is also the reason for repeated predicted values as shows below
Predicted values vs Actual values:
Predicted: 808.94, Actual: 930.00
Predicted: 1209.55, Actual: 875.00
Predicted: 808.94, Actual: 594.00
Predicted: 808.94, Actual: 1143.00
Predicted: 1209.55, Actual: 904.00
Predicted: 1209.55, Actual: 1259.00
Predicted: 408.32, Actual: 429.00
Predicted: 1209.55, Actual: 967.00
Predicted: 808.94, Actual: 573.00
Predicted: 1209.55, Actual: 679.00
Predicted: 808.94, Actual: 611.00
Predicted: 808.94, Actual: 749.00 
Mean Squared Error (MSE): 64765.69 => RMSE = 254.5

The RMSE is also higher due to the way of the dataset was provded and choosing of the sizes in each interval.

It is no secret that Toronto residents are facing down a massive housing crisis. According to a [TMU study](https://www.torontomu.ca/content/dam/social-innovation/Programs/Affordable_Housing_Visual_Systems_Map_Oxford.pdf), the demand for Social housing has increased 68% since 2007, while the amount available has remained largely unchanged. Through our investigation, we have highlighted the incredible diversity of prices real estate properties. And yet, it is obvious that most units skew to the more expensive end. For those struggling to find housing, the question thus remains: what can be done? Has the gentrification of Toronto's neighborhoods gone too far?

Other parties that may be interested in trends in real estate prices may include investors, government bodies, and home owners. With regards to investors, there is the expected trend that larger units with more bedrooms are more valuable. However, it is important to consider whether the prohibitive cost of some of these larger units may make selling them more difficult. This information is also pertinent for home buyers, who can use it to investigate what kinds of units are in their price range.

The information about how prices vary across neighborhoods may be useful for the government. They can determine property tax rates for housing based on the projected valuation of real estate properties by neighborhood.

## 7. Discussion 🗣️
  
The densely packed vertical clusters suggests varying prices for the same size indicating the influence of other variables such as location, age of property etc. Businesses and investors can use this information to price properties competitively based on market trends. They could target different customer segments based on these price patterns such as the central 50% of the price is in the range 551000 to 1681000 CAD which is the main market segment. 
The varying price can also be indicative of a volatile market suggesting that investors should analyze whether these outliers are justifies by other property features before moving forward. Some of the high-price outliers indicate luxury properties which could be potential negotiation oppurtunities. 


