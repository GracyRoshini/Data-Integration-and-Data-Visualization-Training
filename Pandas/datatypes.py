import pandas as pd

df=pd.read_csv("winemag-data-130k-v2.csv",index_col=0)
#df=pd.read_csv("winemad-data-without-null.csv",index_col=0)

print("------------------------------------------------------")

# df.dtypes
# print(df.dtypes)  #Shows the datatype of each column

print("------------------------------------------------------")

#### df.astype() -- type conversion
# df['points']=df['points'].astype('Int32')
# df['country']=df['country'].astype('string')

# print(df.dtypes)

print("------------------------------------------------------")

#### pd.to_numeric()  -- 📌 Convert column to numeric
# df['price']=pd.to_numeric(df['price'],errors='coerce')  #invalid parsing results in NaN (null)
# print(df['price'].head(10))

print("------------------------------------------------------")

#### autmatic Type conversion
# df=df.convert_dtypes()

print("------------------------------------------------------")

#### df.isnull() or df.isna()
# # Returns a DataFrame of booleans where True indicates a NaN.
# print(df.isnull().head(5)[['country','price','points']])
# print(df.isna().head(5)[['country','price','points']])

print("------------------------------------------------------")

#### df.notnull() df.notna()
# masked_df=df['price'].notnull()
# print(masked_df.head(3)) # masking or boolean indexing
###or
#print(df[df['price'].notnull()].head(30))  #Filters only rows where 'price' is not null

print("------------------------------------------------------")

#### isnull
#print(df.isnull().sum())  #Returns count of missing values per column
#print(df['price'].isnull().sum())

print("------------------------------------------------------")

####Creates a mask for rows that have any null values and displays them.
# mask=df.isnull().any(axis=1)
# print(df[mask].head())
###or
#print(df.isnull().any(axis=1).head())

print("------------------------------------------------------")

#####Handling Null Values
#### fillna
###Replaces missing prices with the column's median value
# df['price']=df['price'].fillna(df['price'].median())
# print(df['price'])

print("------------------------------------------------------")

###Replaces missing values with 0
# print('original data price')
# print(df['price'].head(35))
# df['price']=df['price'].fillna(0)

# print('after modified')
# print(df['price'].head(35))

print("------------------------------------------------------")

#####Forward Fill
####ffill: fills missing data with the value from the previous row
# print('original data')
# print(df[['country','price','region_1']].head(15))

# df_ffill=df[['country','price','region_1']].copy()
# df_ffill.ffill(inplace=True)   #inplace: telling pandas to perform the operation directly on the original DataFrame, without returning a new one

# print('After Forward Fill')
# print(df_ffill.head(15))

print("------------------------------------------------------")

#####Backward Fill (bfill)
####bfill: fills missing data with the value from the next row
# print('original data')
# print(df[['country','price','region_1']].head(15))

# df_bfill=df[['country','price','region_1']].copy()
# df_bfill.bfill(inplace=True)

# print('After Backward Fill')
# print(df_bfill.head(15))

print("------------------------------------------------------")

#####Dropping Null Rows
####dropnda()
###Drops entire rows with any NaN values
# total_rows=len(df) # total no of rows in original dataset
# row_with_nulls=df.isnull().any(axis=1).sum() #calculate no.of.rows with  null values in any column
# print(f"total Rows before Drop :{total_rows}")
# print(f"Total Number of Rows with Nulls before Drop: {row_with_nulls}")
df=df.dropna()
print()
print('\n After Dropping rows with Null')
print(f"Remaining Rows: {len(df)}")
print(f"Rows with Null after drop :{df.isnull().any(axis=1).sum()}")
print(f"Total Rows after dropped with null values {df.isnull().sum()}")

print("------------------------------------------------------")

####Exporting Cleaned Data
# df.to_csv("winemad-data-without-null.csv")  #created successfully

print("------------------------END---------------------------")
