import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("winemag-data-130k-v2.csv",index_col=0)

country_counts=df['country'].value_counts().head(20)

plt.figure(figsize=(10,5))  #10 inches wide and 5 inches tall
country_counts.plot(kind="bar",color="pink")
plt.title("Top 20 wine - Producing Countries")
plt.xlabel("Country")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=45)
plt.tight_layout()  #Adjusts padding and spacing automatically
plt.show()