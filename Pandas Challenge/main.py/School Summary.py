#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Load the school data
school_data = pd.read_csv(r'C:\Users\Horva\Downloads\Starter_Code (6)\Starter_Code\PyCitySchools\Resources\schools_complete.csv')

# Load the student data
student_data = pd.read_csv(r'C:\Users\Horva\Downloads\Starter_Code (6)\Starter_Code\PyCitySchools\Resources\students_complete.csv')

# Calculate the total students and total school budget for each school
school_students = student_data.groupby('school_name')['Student ID'].count()
school_budget = school_data.set_index('school_name')['budget']

# Calculate the per student budget
per_student_budget = school_budget / school_students

# Calculate the average math score and average reading score for each school
school_avg_math_score = student_data.groupby('school_name')['math_score'].mean()
school_avg_reading_score = student_data.groupby('school_name')['reading_score'].mean()

# Calculate the percentage of students passing math, passing reading, and overall passing for each school
school_passing_math_percent = (student_data[student_data['math_score'] >= 70].groupby('school_name')['Student ID'].count() / school_students) * 100
school_passing_reading_percent = (student_data[student_data['reading_score'] >= 70].groupby('school_name')['Student ID'].count() / school_students) * 100
school_overall_passing_percent = (student_data[(student_data['math_score'] >= 70) & (student_data['reading_score'] >= 70)].groupby('school_name')['Student ID'].count() / school_students) * 100

# Create the School Summary DataFrame
school_summary = pd.DataFrame({
    'School Name': school_data['school_name'],
    'School Type': school_data['type'],
    'Total Students': school_students,
    'Total School Budget': school_budget,
    'Per Student Budget': per_student_budget,
    'Average Math Score': school_avg_math_score,
    'Average Reading Score': school_avg_reading_score,
    '% Passing Math': school_passing_math_percent,
    '% Passing Reading': school_passing_reading_percent,
    '% Overall Passing': school_overall_passing_percent
})

# Print the School Summary DataFrame
print("School Summary:")
print(school_summary)


# In[ ]:




