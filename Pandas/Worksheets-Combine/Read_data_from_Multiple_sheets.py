import pandas as pd

file_path="CustomerSales_2025.xlsx"

## pd.ExcelFile(file_path) - It doesn't load the full file into memory—just builds access to its contents
## .sheet_names - Returns a list of all worksheet names in that Excel file
sheet_names=pd.ExcelFile(file_path).sheet_names

# print(sheet_names)

# ## sheet_names[0] - grabbing the first sheet in the list
# df_jan=pd.read_excel(file_path,sheet_name=sheet_names[0])
# print("jan Data\n")
# print(df_jan)

# ## sheet_names[1] - grabbing the second sheet in the list
# df_feb=pd.read_excel(file_path,sheet_name=sheet_names[1])
# print("\n Feb data \n")
# print(df_feb)

df_combined=pd.concat([
    pd.read_excel(file_path,sheet_name=sheet) 
    for sheet in sheet_names
])

df_combined.reset_index(drop=True,inplace=True)

# print(df_combined)

## Exporting this combined sheets into another csv file
# df_combined.to_csv("CustomerSales2025Combined.csv")
