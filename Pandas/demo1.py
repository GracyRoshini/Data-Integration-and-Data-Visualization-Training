import pandas as pd
#print(pd.__version__)

#Data Creation
#Data Clean Up
#Data Transformation

#df1=pd.DataFrame({'Team 1':[24,12,9], 'Team 2':[5,12,14]})
#print (df1)

#df2=pd.DataFrame({'customer 1': ['Product was Good','worth for cost'],
#                  'customer 2': ['Moderate Quality', 'Not as expected']},
#                   index=['comment 1','comment 2'])

#print(df2)

#oddseries=pd.Series([10,30,50,70],
#                    index=['row 1','Row 2','Row 3','Row 4'],
#                    name='Odd Numbers')
#print(oddseries)

wine_reviews=pd.read_csv("winemag-data-130k-v2.csv")
print(wine_reviews.shape)

#print(wine_reviews.head())

#Select Colns
#print(wine_reviews.country)

print(wine_reviews['country'])

#print(wine_reviews['country'].iloc[5])
#print(wine_reviews.iloc[0])
#print(wine_reviews.iloc[:,0])
# print(wine_reviews.iloc[:3,1])
# print(wine_reviews.iloc[[1,3,4,6],1])
# print(wine_reviews.iloc[-5])

#print(wine_reviews.loc[10,'country'])

#print(wine_reviews)

#new_reviews=wine_reviews.loc[:,['country','points','price','winery']]
#print(new_reviews)

#print(wine_reviews.set_index("winery"))

##Conditional Selections
#print(wine_reviews.country=="France")
#print(wine_reviews.loc[wine_reviews.country=="France"])
#print(wine_reviews.loc[(wine_reviews.country=="Italy")&(wine_reviews.price>60)])
#print(wine_reviews.loc[(wine_reviews.country=="Italy")&(wine_reviews.price>60),["country","price"]])
#print(wine_reviews.loc[wine_reviews.country.isin(["italy","France"]),["country","price"]])
#print(wine_reviews.loc[wine_reviews.price.notnull()])
# wine_reviews['test column']="test 1"
# print(wine_reviews.head())

#print(wine_reviews.describe())
#print(wine_reviews.country.describe())
#print(wine_reviews.points.mean())
# print(wine_reviews.title.mean())
#print(wine_reviews.title.unique())
#print(wine_reviews.country.value_counts().get("Argentina"))
print((wine_reviews.country=="Spain").sum())
print(wine_reviews.loc[wine_reviews.country=="Spain"].shape[0])