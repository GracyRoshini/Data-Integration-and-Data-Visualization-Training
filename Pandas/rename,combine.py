#### Step 1: Importing pandas
import pandas as pd

#### Step 2: Load the dataset (CSV file)
df=pd.read_csv("winemag-data-130k-v2.csv",index_col=0)

print("------------------------------------------------------")

#### Step 3: Display Initial Columns
# print("Initial Columns",df.columns.tolist())

print("------------------------------------------------------")

#### Step 4: Rename columns for readability
df.rename(columns={
   'country':"Country",
   'description':"Description",
   'designation':"Designation", 
   'points':'Points', 'price':"Price", 'province':"Province", 
   'region_1':"Region", 'region_2':"SubRegion", 
   'taster_name':"Reviewer", 'taster_twitter_handle':"Twitter", 
   'title':"WineTitle", 'variety':"Grape", 'winery':"Winery" 
},inplace=True)

# print("Renamed  Columns",df.columns.tolist())

print("------------------------------------------------------")

#### Step 5: Create a new column that summarizes wine info
### Combines 3 important columns into one to give a quick overview of each wine
df['Wine_Overview']=df['WineTitle']+" | "+df["Grape"]+" | "+df['Winery']

# print(f"\n  Total Columns: {len(df.columns)}")
# print(f"\n {df['Wine_Overview']}")

print("------------------------------------------------------")

#### Step 6: Replace country values
df['Country']=df['Country'].replace({
    "US":"United States of America",
    "England":"United Kingdom",
})

# print(df['Country'].head(10))

print("------------------------------------------------------")

#### Step 7: Filter wines with Points > 90
# high_rated_wines=df[df['Points']>90].copy()
# print(high_rated_wines[['Country','WineTitle','Points']].head(20))

# print(f"\nBefore fillna null rows count {high_rated_wines.isnull().sum()}")
# high_rated_wines['Price']=high_rated_wines['Price'].fillna(1)

# print(f"\n After fillna null rows count {high_rated_wines.isnull().sum()}")

print("------------------------------------------------------")

#### Step 8: Fill missing prices with value 1
# df.fillna({'Price':1},inplace=True)
# print(df['Price'])

print("------------------------------------------------------")

#### Step 9: Create Price Category based on price range
df['PriceCategory']=pd.cut(df['Price'],bins=[0,20,50,100,500,1000],
                           labels=['Budget','Standard','Good','Premium','Luxury'])

print(df[['Country','Price','PriceCategory']])

print("------------------------------------------------------")

#### Step 10: Print column data types
# print(df.dtypes)

print("------------------------------------------------------")

#### Step 11: Save the cleaned data to a new CSV file
# df.to_csv('new_winemag.csv',index=False)

print("------------------------END---------------------------")