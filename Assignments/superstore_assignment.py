# Task 1: Extract and Preview the Data 
# Q1. The Superstore sales team has shared a new CSV file. 
# Load the dataset and give a preview of the top 5 records 
# to validate its structure. Load Superstore.csv into a DataFrame. 
# Check number of rows and columns. Display column names with data types.

import pandas as pd

df=pd.read_csv("Superstore.csv")

# print(df.head())

# print("Rows and Columns: ",df.shape)

# print("\nColumn Info: ")
# print(df.dtypes)

print("---------------------------------------------------------------")

# Task 2: Clean Column Names and Normalize Dates
# Q2. Some columns have inconsistent names with spaces and 
# slashes. Also, the dates are strings. Clean the column names and 
# convert Order Date and Ship Date to datetime format 
# so that you can later group data by month.
# Clean column headers using .str.replace().
# Convert Order_Date and Ship_Date to datetime64.

df.columns = df.columns.str.replace(' ', '_').str.replace('/', '_')
# print(df.columns)

df['Order_Date'] = pd.to_datetime(df['Order_Date'],dayfirst=True)
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'],dayfirst=True)

# print(df['Order_Date'].head(10))
# print(df['Ship_Date'].head(10))

print("---------------------------------------------------------------")

# Task 3: Profitability by Region and Category
# Q3. The regional manager wants to know which region and 
# category combinations are most profitable. 
# Summarize total Sales, Profit, and average Discount 
# grouped by Region and Category.
# Use groupby() + agg() to generate the report.
# Identify which Region+Category had highest profit.

# Group and summarize
profit_report = df.groupby(['Region', 'Category']).agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Discount': 'mean'
}).reset_index()

# Highest profit combo
highest_profit = profit_report.sort_values(by='Profit', ascending=False).head(1)

# print(profit_report)
# print("\nMost Profitable Region + Category:\n")
# print(highest_profit)

print("---------------------------------------------------------------")

# Task 4: Top 5 Most Profitable Products
# Q4. The product team is planning to promote high-profit items. 
# Identify the top 5 products that contributed the most to overall profit.
# Group by Product_Name, sum profit, sort descending, and take top 5.

top_products = df.groupby('Product_Name')['Profit'].sum().sort_values(ascending=False).head(5)

# print("\nTop 5 Products by Profit:\n")
# print(top_products)

print("---------------------------------------------------------------")

# Task 5: Monthly Sales Trend
# Q5. The leadership team wants to review monthly sales performance 
# to understand seasonality. Prepare a month-wise sales trend report.
# Extract month from Order_Date
# Group by month and sum Sales

df['Order_Month'] = df['Order_Date'].dt.to_period('M')  #dt - datetime properties

monthly_sales = df.groupby('Order_Month')['Sales'].sum().reset_index().head(10)

# print("\nMonthly Sales Trend:")
# print(monthly_sales)

print("---------------------------------------------------------------")

# Task 6: Cities with Highest Average Order Value
# Q6. The business is interested in targeting high-value cities for marketing. 
# Calculate the average order value (Sales ÷ Quantity) for each city 
# and list the top 10. Create a new column Order_Value
# Group by City and calculate average order value,Sort and get top 10

# New column for order value
df['Order_Value'] = df['Sales'] / df['Quantity']

# Group by city and calculate average
order_value = df.groupby('City')['Order_Value'].mean().sort_values(ascending=False).head(10)

# print("\nTop 10 Cities by Avg Order Value:")
# print(order_value)

print("---------------------------------------------------------------")

# Task 7: Identify and Save Orders with Loss
# Q7. Finance wants to analyze all loss-making orders. 
# Filter all records where Profit < 0 and save it to a new file 
# called loss_orders.csv 
# Use boolean filtering
# Export the filtered DataFrame to a CSV file without index

# Filter loss-making orders
loss_orders = df[df['Profit'] < 0]

# Export to CSV
loss_orders.to_csv('loss_orders.csv', index=False) #CSV file without index

# print("\nSaved loss-making orders to loss_orders.csv")

print("---------------------------------------------------------------")

# Task 8: Detect Null Values and Impute
# Q8. Are there any missing values in the dataset? 
# If yes, identify columns with nulls and fill missing Price values with 1.
# Use isnull().sum()
# Apply fillna() only on Price column

# Check for nulls
null_counts = df.isnull().sum()
print("\nMissing Value Summary:")
print(null_counts[null_counts > 0])

df=df[df['Quantity']!=0]

df['Calculated_Price']=df['Sales']/df['Quantity']

df['Calculated_Price']=df['Calculated_Price'].fillna(1)

print("-----------------------------END-------------------------------")