#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd

# Load the school data
school_data = pd.DataFrame({
    'School ID': [0, 1, 2, 3, 4],
    'school_name': [
        'Huang High School', 'Figueroa High School', 'Shelton High School', 'Hernandez High School',
        'Griffin High School'
    ],
    'type': [
        'District', 'District', 'Charter', 'District', 'Charter'
    ],
    'size': [2917, 2949, 1761, 4635, 1468],
    'budget': [1910635, 1884411, 1056600, 3022020, 917500]
})

# Load the student data
student_data = pd.DataFrame({
    'Student ID': [0, 1, 2, 3, 4],
    'student_name': [
        'Paul Bradley', 'Victor Smith', 'Kevin Rodriguez', 'Dr. Richard Scott', 'Bonnie Ray'
    ],
    'gender': ['M', 'M', 'M', 'M', 'F'],
    'grade': ['9th', '12th', '12th', '12th', '9th'],
    'school_name': [
        'Huang High School', 'Huang High School', 'Huang High School', 'Huang High School', 'Huang High School'
    ],
    'reading_score': [66, 94, 90, 67, 97],
    'math_score': [79, 61, 60, 58, 84]
})

# Calculate the total number of unique schools
total_schools = school_data['school_name'].nunique()

# Calculate the total number of students
total_students = student_data['Student ID'].nunique()

# Calculate the total budget
total_budget = school_data['budget'].sum()

# Calculate the average math score
avg_math_score = student_data['math_score'].mean()

# Calculate the average reading score
avg_reading_score = student_data['reading_score'].mean()

# Calculate the percentage of students passing math
passing_math_percent = (student_data['math_score'] >= 70).mean() * 100

# Calculate the percentage of students passing reading
passing_reading_percent = (student_data['reading_score'] >= 70).mean() * 100

# Calculate the overall passing percentage
overall_passing_percent = (
    (student_data[(student_data['math_score'] >= 70) & (student_data['reading_score'] >= 70)]['Student ID'].nunique() / total_students)
    * 100
)

# Create the district summary DataFrame
district_summary = pd.DataFrame({
    'Total Schools': [total_schools],
    'Total Students': [total_students],
    'Total Budget': [total_budget],
    'Average Math Score': [avg_math_score],
    'Average Reading Score': [avg_reading_score],
    '% Passing Math': [passing_math_percent],
    '% Passing Reading': [passing_reading_percent],
    '% Overall Passing': [overall_passing_percent]
})

# Print the district summary
print("District Summary:")
print(district_summary)

