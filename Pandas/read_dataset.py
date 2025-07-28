from textblob import TextBlob

import pandas as pd

df=pd.read_csv("Student Attendance datasheet.csv")

# print(df.head())

# print(df.columns)

# print("\nColumn DataType Info: ")
# print(df.dtypes)

summary_list = []

print("------------------------------------------------------------")


#### Q1. Attendance Percentage by Gender

df['Attendance %'] = (df['Attendance Status'] / 100) * 100
attendance_Status_by_gender=df.groupby('Gender')['Attendance %'].mean()
print(attendance_Status_by_gender.round(2).astype(str) + '%')
summary_list.append(attendance_Status_by_gender)

print("------------------------------------------------------------")


#### Q2. Attendance Percentage by Job Level

df['Attendance %'] = (df['Attendance Status'] / 100) * 100  
attendance_Status_by_job_level = df.groupby('Job Level')['Attendance %'].mean()
print(attendance_Status_by_job_level.round(2).astype(str) + '%')
summary_list.append(attendance_Status_by_job_level)

print("------------------------------------------------------------")


#### Q3. Attendance Percentage by Team

df['Attendance %'] = (df['Attendance Status'] / 100) * 100  
attendance_Status_by_team = df.groupby('Team')['Attendance %'].mean()
print(attendance_Status_by_team.round(2).astype(str) + '%')
summary_list.append(attendance_Status_by_team)

print("------------------------------------------------------------")


#### Q4. Attendance Percentage by Location

df['Attendance %'] = (df['Attendance Status'] / 100) * 100  
attendance_Status_by_location = df.groupby('Please select your location')['Attendance %'].mean() #Please select your location - coln name
print(attendance_Status_by_location.round(2).astype(str) + '%')

print("------------------------------------------------------------")


#### Q5. Bonus Distribution by Gender

Bonus_by_Gender=df.groupby('Gender')['Bonus'].mean() #['Bonus'] - Name: Bonus in output
print(Bonus_by_Gender)

print("------------------------------------------------------------")


#### Q6. Salary Trends by Job Level

sal_trend_by_job_level=df.groupby('Job Level')['Salary'].mean()
print(sal_trend_by_job_level)

print("------------------------------------------------------------")


#### Q7. Training Completion Rate by Quarter by Gender

Training_completion_rate_by_Gender=df.groupby(['Quarter','Gender'])['Training'].value_counts(normalize=True).unstack() * 100
print(Training_completion_rate_by_Gender.round(2).astype(str) + '%')

print("------------------------------------------------------------")


#### Q8. Feedback Sentiment by Team

# Step 1: Create a new column with sentiment polarity
# Converts the raw text (feedback) into a TextBlob object, which gives access to NLP (natural language processing) features like sentiment
# .sentiment.polarity It returns a number between:
# -1.0 → Very negative
# 0 → Neutral
# +1.0 → Very positive

# Step 1: Create a new column with sentiment polarity
df['Sentiment Score'] = df['Please enter your feedback'].apply(lambda text: TextBlob(text).sentiment.polarity)

# Step 2: Group by Team and calculate average sentiment
feedback_sentiment_by_team = df.groupby('Team')['Sentiment Score'].mean()# print(Feedback_sentiment_by_team)

# Step 3: Convert to percentage out of 100
# + 1 = Shift so there's no negatives, *50 = 0 to 100	Convert to percentage scale
feedback_sentiment_percentage = (feedback_sentiment_by_team + 1) * 50 

print(feedback_sentiment_percentage.round(2).astype(str) + '%')

print("------------------------------------------------------------")


#### Q9. Average Bonus by Quarter
avg_bonus_by_quarter=df.groupby('Quarter')['Bonus'].mean()
bonus_percentage = (avg_bonus_by_quarter / df['Bonus'].max()) * 100
print(bonus_percentage.round(2).astype(str) + '%')

print("------------------------------------------------------------")


#### Q10. Salary Trends by Location
salary_trends_by_loc=df.groupby('Please select your location')['Salary'].mean()
salary_percentage = (salary_trends_by_loc / salary_trends_by_loc.max()) * 100
print(salary_percentage.round(2).astype(str) + '%')

print("---------------------------END------------------------------")


#### Q11. Average Present & Absent by Gender, Location, Job level, Team
def attendance_summary_by(attribute):
    present = df[df['Attendance'] == 'Present'].groupby(attribute)['Attendance Status'].mean().round(2)
    absent = df[df['Attendance'] == 'Absent'].groupby(attribute)['Attendance Status'].mean().round(2)

    return pd.DataFrame({
        'Average Present Days': present,
        'Average Absent Days': absent
    })

# Apply function to each category
gender_summary = attendance_summary_by('Gender')
location_summary = attendance_summary_by('Please select your location')
joblevel_summary = attendance_summary_by('Job Level')
team_summary = attendance_summary_by('Team')

# Display the results
print("Attendance Summary by Gender:\n", gender_summary.astype(str) + '%')
print("\nAttendance Summary by Location:\n", location_summary.astype(str) + '%')
print("\nAttendance Summary by Job Level:\n", joblevel_summary.astype(str) + '%')
print("\nAttendance Summary by Team:\n", team_summary.astype(str) + '%')


print("------------------------------------------------------------")


# Step 1: Attendance % and Sentiment columns are calculated
df['Attendance %'] = (df['Attendance Status'] / 100) * 100
df['Sentiment Score'] = df['Please enter your feedback'].apply(lambda text: TextBlob(str(text)).sentiment.polarity)
df['Sentiment %'] = (df['Sentiment Score'] + 1) * 50

# Step 2: Collect summaries
summary_data = {}

# Q1: Attendance % by Gender
summary_data['Attendance % by Gender'] = df.groupby('Gender')['Attendance %'].mean().round(2)

# Q2: Attendance % by Job Level
summary_data['Attendance % by Job Level'] = df.groupby('Job Level')['Attendance %'].mean().round(2)

# Q3: Attendance % by Team
summary_data['Attendance % by Team'] = df.groupby('Team')['Attendance %'].mean().round(2)

# Q4: Attendance % by Location
summary_data['Attendance % by Location'] = df.groupby('Please select your location')['Attendance %'].mean().round(2)

# Q5: Bonus by Gender
summary_data['Average Bonus by Gender'] = df.groupby('Gender')['Bonus'].mean().round(2)

# Q6: Salary by Job Level
summary_data['Average Salary by Job Level'] = df.groupby('Job Level')['Salary'].mean().round(2)

# Q7: Training Completion Rate by Quarter by Gender
training_summary = df.groupby(['Quarter', 'Gender'])['Training'].value_counts(normalize=True).unstack().fillna(0) * 100
training_summary = training_summary.round(2)

# Q8: Feedback Sentiment % by Team
summary_data['Sentiment % by Team'] = df.groupby('Team')['Sentiment %'].mean().round(2)

# Q9: Bonus % by Quarter
avg_bonus_by_quarter = df.groupby('Quarter')['Bonus'].mean()
summary_data['Bonus % by Quarter'] = ((avg_bonus_by_quarter / df['Bonus'].max()) * 100).round(2)

# Q10: Salary % by Location
salary_by_loc = df.groupby('Please select your location')['Salary'].mean()
summary_data['Salary % by Location'] = ((salary_by_loc / salary_by_loc.max()) * 100).round(2)

# Q11: Attendance Summary Function
def attendance_summary_by(attribute):
    present = df[df['Attendance'] == 'Present'].groupby(attribute)['Attendance Status'].mean().round(2)
    absent = df[df['Attendance'] == 'Absent'].groupby(attribute)['Attendance Status'].mean().round(2)
    return pd.DataFrame({
        f'Average Present by {attribute}': present,
        f'Average Absent by {attribute}': absent
    })

# Attendance summaries
gender_attendance = attendance_summary_by('Gender')
location_attendance = attendance_summary_by('Please select your location')
joblevel_attendance = attendance_summary_by('Job Level')
team_attendance = attendance_summary_by('Team')

# Step 3: Merge all into a single DataFrame (with outer joins)
summary_df = pd.DataFrame()















