import pandas as pd
import pyodbc

conn = pyodbc.connect(
    r'DRIVER={SQL Server};'
    r'SERVER=GRACY\SQLEXPRESS;'
    r'DATABASE=Hexa_22jul_DB;'
    r'Trusted_Connection=yes;'
)

query="SELECT * FROM CustomerOrders"
df=pd.read_sql(query,conn)


# print("📝Raw data")
# print(df.head())


# # Basic Data Cleaning
# df['CustomerName']=df['CustomerName'].str.strip().str.title();
# print(df['CustomerName'])


# mask=df['Email'].fillna('').str.contains(r'[A-Z]')  #email id w full Caps
# upper_case_emails=df[mask]
# print(upper_case_emails.head(10))


# df['Email'].str.lower()
# df['Quantity'] = df['Quantity'].fillna(1)
# df['PricePerUnit'] = df['PricePerUnit'].fillna(df['PricePerUnit'].mean())
# df['OrderDate'] = df['OrderDate'].ffill()


# df['CleanedName'] = df['CustomerName'].str.strip().str.upper()


# # find duplicates
# duplicate_names = df[df.duplicated('CleanedName', keep=False)]
# print("Duplicated Records")
# print(duplicate_names)


# df_cleaned=df.drop_duplicates()
# duplicates=df_cleaned[df_cleaned.duplicated(keep=False)]
# print("\n After Removed Duplicated Records")
# print(duplicates)


# df_cleaned['Total Price']=df_cleaned['Quantity']*df_cleaned['PricePerUnit']


# print(df_cleaned.head())


# df_cleaned.to_csv("Cleaned_customer_Orders_Data.csv")
