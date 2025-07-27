import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)  #sets the first column as the index

print(df.iloc[-5]) #to print 5th record from last
print(df.loc[8,'country'])  #label based filter on row country coln 8th index value

england_df=df[df['country']=='England'] #Filters rows where the country is "England" and stores them in a new DataFrame
print(england_df.count()) #Prints non-null count of each column

#To print last 5 records
print(df.tail())


# Step 2: Show initial data
print("🔹 Initial Data Sample:")
print(df[['country', 'price', 'points']].head(5))  #Prints the first 5 rows of selected columns


# Step 3: Map Country Names
country_map = {
    "US": "USA",
    "England": "UK",
    "South Korea": "Korea"
}  #Creates a dictionary to standardize country names.

print('Before Standardized',len(df.columns)) #Prints the number of columns before adding the new column

df['country_standardized'] = df['country'].map(country_map).fillna(df['country']) #.map() to replace values based on country_map
#.fillna(df['country']) keeps original value if no match is found in the map

print('After Standardized',len(df.columns)) #Prints the number of columns after adding country_standardized
print(df.head(3))


# Step 4: Apply Price Category Logic  --Creating a new coln for categorize based on price range using apply method
def price_category(price):
    if pd.isna(price): #Pandas function that checks if a value is NaN. If price is NaN, this condition will return True
        return "Unknown"
    elif price < 20:
        return "Budget"
    elif price < 50:
        return "Standard"
    elif price < 100:
        return "Premium"
    else:
        return "Luxury"

df['price_category'] = df['price'].apply(price_category)


# Step 5: Map points to grades
df['points_grade'] = df['points'].map(lambda x: 'High' if x >= 90 else 'Low')

df['quality_label']=df['points'].apply(lambda x:
                                       'Excellent' if x>=95 else 
                                       'Very Good' if x>=90 else
                                       'Good' if x>=85 else
                                       'Average')


print(len(df.columns))
print(df.head(3))


# Step 6: Apply row-wise transformation to create a summary
def summarize(row): #Defines a function to return a summary string for each row
    return f"{row['country']} - {row['variety']} - {row['points']} pts"

df['summary'] = df.apply(summarize, axis=1) #Applies the summarize function row by row to create a new column summary


# Step 7: Show Transformed Columns
print("\n🔸 Transformed Sample:")
#Shows the first 10 rows of selected transformed columns
print(df[['country', 'country_standardized', 'price', 'price_category', 'points', 'points_grade', 'summary']].head(10))


# Step 8: Optional - Save to CSV
df.to_csv("transformed_winemag_data.csv", index=False) #index=False prevents saving the index as a separate column
print("\n✅ Transformed data saved to 'transformed_winemag_data.csv'")