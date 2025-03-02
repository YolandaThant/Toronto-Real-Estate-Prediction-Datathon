import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.linear_model import LinearRegression


# read the data from the dataset
data = pd.read_csv("cleaned_real_estate_data.csv")

# make it into a dataframe
df = pd.DataFrame(data)

size = df['size']
summary = size.describe()
print(summary)
# plot the graph
graph = sns.jointplot(x = "size", y = "price (In 1000s)", 
              data = df, kind = "reg", scatter_kws={'color': 'limegreen'}, line_kws={'color': 'darkgreen', 'linewidth': 2}, marginal_kws={'color': 'green'}) 

# title of the figure
graph.figure.suptitle("Joint plot for size (square feet) vs Price", fontsize = 12)


# show the plot 
plt.show() 
