import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd

# read the data from the dataset
data = pd.read_csv("cleaned_real_estate_data.csv")

# make it into a dataframe
df = pd.DataFrame(data)

# plot the graph
graph = sns.jointplot(x = "size", y = "price (In 1000s)", 
              data = df, kind = "reg", scatter_kws={'color': 'limegreen'}, line_kws={'color': 'darkgreen', 'linewidth': 2}, marginal_kws={'color': 'green'}) 

# title of the figure
graph.figure.suptitle("Size (square feet) vs Price", fontsize = 12)

# show the plot 
plt.show() 