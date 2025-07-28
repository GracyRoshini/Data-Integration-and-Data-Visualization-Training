import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data={
    "Time_Spent_Ads":[230,44,17,151,180,20,89,134,65,90],
    "Sales":[22,10,8,17,20,6,13,16,11,12]
}
df=pd.DataFrame(data)

# # Scatter Plot
# sns.scatterplot(x="Time_Spent_Ads",y="Sales",data=df)
# plt.title("Ads Vs Sales")
# plt.xlabel("Ad Spend (k)")
# plt.ylabel("Sales (units)")
# plt.show()


df['Time_Category']=pd.cut(df['Time_Spent_Ads'],
                           bins=[0,50,100,150,200,250],
                           labels=["0-50","51-100","101-150","151-200","201-250"])

# Box Plot
sns.boxplot(x="Time_Category",y="Sales",data=df)
plt.title("Sales based Ads")
plt.xlabel("time Spent on Ads")
plt.ylabel("Sales")
plt.show()