import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
dataset = pd.read_csv("cleaned_real_estate_data.csv")
dataset

#group by bedrooms

beds_0 = dataset.loc[dataset['beds'] == 0, ['price (In 1000s)','beds']]
beds_0

beds_1 = dataset.loc[dataset['beds'] == 1, ['price (In 1000s)','beds']]
beds_1

beds_2 = dataset.loc[dataset['beds'] == 2, ['price (In 1000s)','beds']]
beds_2

beds_3 = dataset.loc[dataset['beds'] == 3, ['price (In 1000s)','beds']]
beds_3

#bedroom dataset

beds_0_price = beds_0['price (In 1000s)'] 
beds_1_price = beds_1['price (In 1000s)'] 
beds_2_price = beds_2['price (In 1000s)'] 
beds_3_price = beds_3['price (In 1000s)']

bedrooms = [beds_0_price, beds_1_price, beds_2_price, beds_3_price]

import matplotlib.cm as cm

#create a boxplot
fig, ax = plt.subplots()
box = plt.boxplot(bedrooms, vert=False, patch_artist=True, positions=[1,2,3,4], medianprops={'color':'black', 'linewidth':2})

#rainbow
cmap = cm.ScalarMappable(cmap='rainbow')
box_mean = [np.mean(x) for x in bedrooms]
for patch, color in zip(box['boxes'], cmap.to_rgba(box_mean)):
    patch.set_facecolor(color)


#label boxplot
plt.yticks([1,2,3,4], ['Studio', '1 Bedroom', '2 Bedroom', '3 Bedroom'], rotation=0)
plt.title('Apartment Type vs. Price (In 1000s)', pad=10)
plt.xlabel('Price (In 1000s)', labelpad = 20)
plt.ylabel('Apartment Type', rotation=90, labelpad = 20)

#show boxplot
plt.show()