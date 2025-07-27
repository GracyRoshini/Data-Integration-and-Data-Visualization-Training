import pandas as pd
import numpy as np

# Load original dataset
df = pd.read_csv('updated_college_student_placement_dataset.csv')

# Add test rows covering all Que 14–18 cases
test_rows = pd.DataFrame([
    # Row with missing Salary (Que 14)
    {
        'College_ID': 'T001', 'IQ': 115, 'Prev_Sem_Result': 82, 'CGPA': 8.1, 'Academic_Performance': 'Good',
        'Internship_Experience': 'Yes', 'Extra_Curricular_Score': 78, 'Communication_Skills': 'High',
        'Projects_Completed': 4, 'Placement': 'Yes', 'Gender': 'Male', 'MBA_Percentage': 75.5,
        'SSC_Percentage': 84.0, 'HSC_Percentage': 83.5, 'Salary': np.nan,
        'placement_success': 'Success', 'Degree_Range': '70-80', 'Salary_Band': None
    },

    # Exact duplicate of above (Que 16)
    {
        'College_ID': 'T001', 'IQ': 115, 'Prev_Sem_Result': 82, 'CGPA': 8.1, 'Academic_Performance': 'Good',
        'Internship_Experience': 'Yes', 'Extra_Curricular_Score': 78, 'Communication_Skills': 'High',
        'Projects_Completed': 4, 'Placement': 'Yes', 'Gender': 'Male', 'MBA_Percentage': 75.5,
        'SSC_Percentage': 84.0, 'HSC_Percentage': 83.5, 'Salary': np.nan,
        'placement_success': 'Success', 'Degree_Range': '70-80', 'Salary_Band': None
    },

    # Same College_ID, different values (Que 18)
    {
        'College_ID': 'T001', 'IQ': 100, 'Prev_Sem_Result': 70, 'CGPA': 7.0, 'Academic_Performance': 'Average',
        'Internship_Experience': 'No', 'Extra_Curricular_Score': 60, 'Communication_Skills': 'Medium',
        'Projects_Completed': 2, 'Placement': 'No', 'Gender': 'Female', 'MBA_Percentage': 65.0,
        'SSC_Percentage': 76.0, 'HSC_Percentage': 72.5, 'Salary': 0.0,
        'placement_success': 'Fail', 'Degree_Range': '60-70', 'Salary_Band': 'Low'
    },

    # Fully complete and unique row (Que 15 filter test)
    {
        'College_ID': 'T999', 'IQ': 130, 'Prev_Sem_Result': 92, 'CGPA': 9.2, 'Academic_Performance': 'Excellent',
        'Internship_Experience': 'Yes', 'Extra_Curricular_Score': 95, 'Communication_Skills': 'Exceptional',
        'Projects_Completed': 5, 'Placement': 'Yes', 'Gender': 'Female', 'MBA_Percentage': 89.0,
        'SSC_Percentage': 93.0, 'HSC_Percentage': 94.0, 'Salary': 750000.0,
        'placement_success': 'Success', 'Degree_Range': '90-100', 'Salary_Band': 'High'
    }
])

# Append these rows to the original DataFrame
df = pd.concat([df, test_rows], ignore_index=True)

# Optional: Save for testing outputs later
df.to_csv('updated_college_student_placement_dataset_test.csv', index=False)
