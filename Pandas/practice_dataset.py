import pandas as pd
from textblob import TextBlob

df=pd.read_csv("Student Attendance datasheet.csv")

# Attendance % column exists
if 'Attendance %' not in df.columns:
    df['Attendance %'] = (df['Attendance Status'] / 100) * 100

# Initialize list to collect all summaries
summary_list = []

# Q1 - Attendance % by Gender
q1 = df.groupby('Gender')['Attendance %'].mean().reset_index().rename(columns={'Gender': 'Group', 'Attendance %': 'Attendance %'})
q1['Category'] = 'Gender'; summary_list.append(q1)

# Q2 - Attendance % by Job Level
q2 = df.groupby('Job Level')['Attendance %'].mean().reset_index().rename(columns={'Job Level': 'Group', 'Attendance %': 'Attendance %'})
q2['Category'] = 'Job Level'; summary_list.append(q2)

# Q3 - Attendance % by Team
q3 = df.groupby('Team')['Attendance %'].mean().reset_index().rename(columns={'Team': 'Group', 'Attendance %': 'Attendance %'})
q3['Category'] = 'Team'; summary_list.append(q3)

# Q4 - Attendance % by Location
q4 = df.groupby('Please select your location')['Attendance %'].mean().reset_index().rename(columns={'Please select your location': 'Group', 'Attendance %': 'Attendance %'})
q4['Category'] = 'Location'; summary_list.append(q4)

# Q5 - Bonus by Gender
q5 = df.groupby('Gender')['Bonus'].mean().reset_index().rename(columns={'Gender': 'Group', 'Bonus': 'Average Bonus'})
q5['Category'] = 'Gender'; summary_list.append(q5)

# Q6 - Salary by Job Level
q6 = df.groupby('Job Level')['Salary'].mean().reset_index().rename(columns={'Job Level': 'Group', 'Salary': 'Average Salary'})
q6['Category'] = 'Job Level'; summary_list.append(q6)

# Q7 - Training Completion Rate 
training_completion = df.groupby(['Quarter', 'Gender'])['Training'].value_counts(normalize=True).unstack().fillna(0) * 100
training_completion.reset_index(inplace=True)
training_completion.to_csv("Training_Completion_Rate.csv", index=False)

# Q8 - Feedback Sentiment % by Team
df['Sentiment Score'] = df['Please enter your feedback'].apply(lambda text: TextBlob(str(text)).sentiment.polarity)
feedback_sentiment = df.groupby('Team')['Sentiment Score'].mean()
feedback_percentage = (feedback_sentiment + 1) * 50
q8 = feedback_percentage.reset_index().rename(columns={'Team': 'Group', 'Sentiment Score': 'Feedback Sentiment %'})
q8['Category'] = 'Team'; summary_list.append(q8)

# Q9 - Bonus % by Quarter
bonus_by_quarter = df.groupby('Quarter')['Bonus'].mean()
bonus_pct = (bonus_by_quarter / df['Bonus'].max()) * 100
q9 = bonus_pct.reset_index().rename(columns={'Quarter': 'Group', 'Bonus': 'Bonus %'})
q9['Category'] = 'Quarter'; summary_list.append(q9)

# Q10 - Salary % by Location
salary_by_loc = df.groupby('Please select your location')['Salary'].mean()
salary_pct = (salary_by_loc / salary_by_loc.max()) * 100
q10 = salary_pct.reset_index().rename(columns={'Please select your location': 'Group', 'Salary': 'Salary %'})
q10['Category'] = 'Location'; summary_list.append(q10)

# Q11 - Present & Absent Summary

def attendance_summary_by(attribute):
    present = df[df['Attendance'] == 'Present'].groupby(attribute)['Attendance Status'].mean().round(2)
    absent = df[df['Attendance'] == 'Absent'].groupby(attribute)['Attendance Status'].mean().round(2)
    return pd.DataFrame({
        'Group': present.index,
        'Average Present Days': present.values,
        'Average Absent Days': absent.reindex(present.index).values,
        'Category': attribute
    })

summary_list.append(attendance_summary_by('Gender'))
summary_list.append(attendance_summary_by('Please select your location'))
summary_list.append(attendance_summary_by('Job Level'))
summary_list.append(attendance_summary_by('Team'))

# Saving final summary
final_summary_df = pd.concat(summary_list, ignore_index=True)
final_summary_df.to_csv("Student_Attendance_Analysis.csv", index=False)

print("✅ 'Student_Attendance_Analysis.csv' and 'Training_Completion_Rate.csv' have been saved.")

# ================= Display Section ====================

# Display Attendance Percentages
print(df.groupby('Gender')['Attendance %'].mean().round(2).astype(str) + '%')
print(df.groupby('Job Level')['Attendance %'].mean().round(2).astype(str) + '%')
print(df.groupby('Team')['Attendance %'].mean().round(2).astype(str) + '%')
print(df.groupby('Please select your location')['Attendance %'].mean().round(2).astype(str) + '%')

# Bonus and Salary
print(df.groupby('Gender')['Bonus'].mean())
print(df.groupby('Job Level')['Salary'].mean())

# Training Completion Display
print(training_completion.round(2).astype(str) + '%')

# Feedback Sentiment
print(feedback_percentage.round(2).astype(str) + '%')

# Bonus % by Quarter
print(bonus_pct.round(2).astype(str) + '%')

# Salary % by Location
print(salary_pct.round(2).astype(str) + '%')

# Present & Absent Summary Display
print("Attendance Summary by Gender:\n", attendance_summary_by('Gender').set_index('Group').astype(str) + '%')
print("\nAttendance Summary by Location:\n", attendance_summary_by('Please select your location').set_index('Group').astype(str) + '%')
print("\nAttendance Summary by Job Level:\n", attendance_summary_by('Job Level').set_index('Group').astype(str) + '%')
print("\nAttendance Summary by Team:\n", attendance_summary_by('Team').set_index('Group').astype(str) + '%')