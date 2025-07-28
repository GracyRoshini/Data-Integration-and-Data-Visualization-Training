import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

# 2. Group by country and calculate the average wine rating (points)
avg_rating_by_country = df.groupby('country')['price'].mean()

# 3. Sort by descending order and get the top 10 countries
top_10_countries = avg_rating_by_country.sort_values(ascending=False).head(10)

# 4. Plot - Horizontal bar chart
plt.figure(figsize=(10, 5))
top_10_countries.plot(kind='barh', color='pink')

# 5. Customize the plot
plt.xlabel('Average Rating (Price)')
plt.ylabel('Country')
plt.title('Top 10 Countries by Average Wine Rating')
# plt.gca().invert_yaxis()  # Put highest rating at the top
plt.tight_layout()

# 6. Show the chart
plt.show()