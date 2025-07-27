import pandas as pd

df=pd.read_csv("final_college_student_placement_dataset.csv")

#print(df.head())
#print(df.columns)

print("---------------------------------------------------------")
print("--Que 1--")

#1. How many students are in the dataset?
print("Total Students: ",len(df))

print("---------------------------------------------------------")
print("--Que 2--")

#2. Display the number of male and female students.
print(df['Gender'].value_counts())

print("---------------------------------------------------------")
print("--Que 3--")

#3. What is the average percentage in MBA?
print("Average MBA %:",df['MBA_Percentage'].mean())

print("---------------------------------------------------------")
print("--Que 4--")

#4. Show students who scored more than 80% in both SSC and HSC.
ssc_hsc_80perc=df[(df['SSC_Percentage']>80) & (df['HSC_Percentage']>80)]
print(ssc_hsc_80perc[['College_ID','SSC_Percentage','HSC_Percentage']])

print("---------------------------------------------------------")
print("--Que 5--")

#5. Filter only students who have prior work experience.
Students_With_Experience=df[df['Internship_Experience']=="Yes"]
print(Students_With_Experience[['College_ID','Internship_Experience']])

print("---------------------------------------------------------")
print("--Que 6--")

#6. Average MBA score per specialization.
mba_avg_specialization = df.groupby('Specialization', observed=True)['MBA_Percentage'].mean()
print(mba_avg_specialization)

print("---------------------------------------------------------")
print("--Que 7--")

#7. Count of placed vs not placed students.
print(df['Placement'].value_counts())

print("---------------------------------------------------------")
print("--Que 8--")

#8. Placement ratio per specialization. 
#Normalizes to get the ratio, not raw count
#unstack() reshapes the result so it's easier to read
placement_ratio = df.groupby('Specialization', observed=True)['Placement'].value_counts(normalize=True).unstack().fillna(0)
print(placement_ratio)

print("---------------------------------------------------------")
print("--Que 9--")

#9. Create a new column placement_success with:
#   "High" if placed and salary > ₹950,000
#   "Average" if placed and salary <= ₹400,000
#   "Unplaced" if not placed
def categorize(row):
    if row['Placement'] == 'Yes' and row['Salary'] > 950000:
        return 'High'
    elif row['Placement'] == 'Yes' and row['Salary'] <= 400000:
        return 'Average'
    elif row['Placement'] == 'No':
        return 'Unplaced'
    else:
        return 'Moderate'  # Optional catch-all

df['placement_success'] = df.apply(categorize, axis=1)
print(df[['College_ID', 'Placement', 'Salary', 'placement_success']])

print("---------------------------------------------------------")
print("--Que 10--")

#10. Among placed students, which degree percentage range leads to highest average salary?
# Create degree percentage bins
degree_percentage = [0, 60, 70, 80, 90, 100]
labels = ['<60%', '60-70%', '70-80%', '80-90%', '90-100%']

df['Degree_Range'] = pd.cut(df['CGPA'], bins=degree_percentage, labels=labels)

# Filter placed students
placed = df[df['Placement'] == 'Yes']

# Group by degree range and compute average salary
result = placed.groupby('Degree_Range',observed=True)['Salary'].mean().sort_values(ascending=False)
print(result)

print("---------------------------------------------------------")
print("--Que 11--")

#11. Categorize placed students into salary bands
placed=df[df['Placement'] == 'Yes']
def categorize_salary(sal):
    if sal < 300000:
        return "Low"
    elif 300000 <= sal <= 600000:
        return "Medium"
    else:
        return "High"

df['Salary_Band'] = placed['Salary'].apply(categorize_salary)
print(df[['Salary', 'Placement', 'Salary_Band']].dropna())  #used for removing missing values

print("---------------------------------------------------------")
print("--Que 12--")

#12. For each gender and specialization, calculate: Placement rate Average salary (only placed) Avg MBA score
grouped = df.groupby(['Gender', 'Specialization'], observed=True)

summary = pd.DataFrame({
    'Placement Rate': grouped['Placement'].apply(lambda x: (x == 'Yes').mean()),
    'Avg Salary (Placed)': grouped.apply(lambda x: x[x['Placement'] == 'Yes']['Salary'].mean()),
    'Avg MBA Score': grouped['MBA_Percentage'].mean()
})

print(summary.reset_index())

print("---------------------------------------------------------")
print("--Que 13--")

#13.Find how many students have missing values in any column
missing_count = df.isnull().any(axis=1).sum()
print(f"Number of students with missing values: {missing_count}")

print("---------------------------------------------------------")
print("--Que 14--")

#14. Display all rows where salary is missing
missing_salary = df[df['Salary'].isnull()]
print(missing_salary)

print("---------------------------------------------------------")
print("--Que 15--")

#15. Filter only students with complete records (no missing values)
complete_records = df.dropna()
print(complete_records.shape)

print("---------------------------------------------------------")
print("--Que 16--")

#16. Identify if there are any duplicate student entries
duplicates = df[df.duplicated()]
print(f"Number of duplicate rows: {duplicates.shape[0]}")

print("---------------------------------------------------------")
print("--Que 17--")

#17. Drop the duplicate records and keep only the first occurrence
df_unique = df.drop_duplicates(keep='first')
print(f"Shape after dropping duplicates: {df_unique.shape}")

print("---------------------------------------------------------")
print("--Que 18--")

#18. Check for duplicates based only on student_id
df_Check_dupl_ID = df.duplicated(subset='College_ID')
print(f"Duplicate entries based on College_ID: {df_Check_dupl_ID.shape[0]}")


print("---------------------------------------------------------")
print("--Que 19--")

#19. Find all unique specializations offered to students
#dropna() removes any missing values
#unique() An array of distinct values	
unique_specializations = df['Specialization'].dropna().unique()
print("Unique Specializations:", unique_specializations)

print("---------------------------------------------------------")
print("--Que 20--")

#20. How many unique MBA scores are there?
#nunique() gives you the count of distinct MBA percentages, excluding missing values
unique_mba_scores = df['MBA_Percentage'].nunique()
print("Number of unique MBA scores:", unique_mba_scores)

print("---------------------------------------------------------")
print("--Que 21--")

#21. Count of unique combinations of gender, specialization, and status
unique_combinations = df[['Gender', 'Specialization', 'Placement']].dropna().drop_duplicates()
print("Number of unique combinations:", unique_combinations.shape[0])
print(unique_combinations)

print("---------------------------------------------------------")
print("--Que 22--")

#22. What is the maximum and minimum degree percentage in the dataset?
max_degree = df['CGPA'].max()
min_degree = df['CGPA'].min()
print(f"Maximum CGPA: {max_degree}")
print(f"Minimum CGPA: {min_degree}")

print("---------------------------------------------------------")
print("--Que 23--")

#23. For each specialization, calculate: Average SSC, Average MBA, Placement count
specialization_summary = df.groupby('Specialization', observed=True).agg({
    'SSC_Percentage': 'mean',
    'MBA_Percentage': 'mean',
    'Placement': lambda x: (x == 'Yes').sum()
}).rename(columns={
    'SSC_Percentage': 'Average SSC',
    'MBA_Percentage': 'Average MBA',
    'Placement': 'Placement Count'
})

print(specialization_summary.reset_index())

print("---------------------------------------------------------")
print("--Que 24--")

#24. Create a summary table with: Column name, Count of nulls, Count of unique values, Duplicated value count (if applicable)
summary_table = pd.DataFrame({
    'Column Name': df.columns,
    'Null Count': df.isnull().sum().values,
    'Unique Count': df.nunique().values,
    'Duplicate Count': [df.duplicated(subset=[col]).sum() if df[col].duplicated().any() else 0 for col in df.columns]
})

print(summary_table)

print("---------------------------------------------------------")
print("--END--")
