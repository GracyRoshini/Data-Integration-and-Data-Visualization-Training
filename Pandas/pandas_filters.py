import pandas as pd

df=pd.read_csv("winemag-data-130k-v2.csv",index_col=0)

# # isin()
# print(df[df['country'].isin(['US','Portugal','Spain'])])

# # str.contains()
# print(df[df['description'].str.contains("Blackberry",case=False,na=False)]
#       ['description'])

# # between
# print(df[df['price'].between(10,30)]['price'])

# # isnull
# print(df[df['price'].isnull()])
# print(df[df['price'].isnull()][['title','price']])

# #not null
# print(df[df['price'].notnull()][['title','price']])

# #Filter Duplicates
# duplcate_df=df[df.duplicated('title',keep=False)] #-keep=False: marks all duplicates, not just the first or last
# print(duplcate_df[['title','points','price']])

# # Keep Only First Occurance and drop the rest
# df_no_duplicates=df.drop_duplicates(subset='title',keep='first') #-Removes duplicate title rows, keeping only the first occurrence
# print(df_no_duplicates[['title','points','price']].head(20))

# # Display unique Row of Title column
# unique_titles=df[df.duplicated('title',keep=False)]['title'].unique()
# print(unique_titles)

# # howmany time each title occurs
# title_counts=df['title'].value_counts();
# print(title_counts[title_counts>1])

# find the Duplicates in Multiple column
multi_column_duplicates=df[df.duplicated(subset=['title','points'],keep=False)]
print(multi_column_duplicates[['title','points','country']])