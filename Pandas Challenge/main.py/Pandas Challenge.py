#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


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


# In[3]:


#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

# Read the School Summary CSV file
school_summary = pd.read_csv(r'C:\Users\Horva\Downloads\Starter_Code (6)\Starter_Code\PyCitySchools\Resources\school_summary.csv')

# Sort the schools by % Overall Passing in descending order and get the top 5 rows
top_schools = school_summary.sort_values(by='% Overall Passing', ascending=False).head(5)

# Display the top performing schools
print("Top Performing Schools:")
print(top_schools)


# In[ ]:


# In[4]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Read the School Summary CSV file
school_summary = pd.read_csv(r'C:\Users\Horva\Downloads\Starter_Code (6)\Starter_Code\PyCitySchools\Resources\school_summary.csv')

# Sort the schools by % Overall Passing in ascending order and get the top 5 rows
bottom_schools = school_summary.sort_values(by='% Overall Passing', ascending=True).head(5)

# Display the lowest performing schools
print("Lowest Performing Schools:")
print(bottom_schools)


# In[ ]:


# In[5]:


#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Read the student data CSV file
student_data = pd.read_csv(r'C:\Users\Horva\Downloads\Starter_Code (6)\Starter_Code\PyCitySchools\Resources\students_complete.csv')

# Pivot the student_data DataFrame to calculate the average math score for each grade and school
math_scores_by_grade = student_data.pivot_table(values='math_score', index='school_name', columns='grade', aggfunc='mean')

# Display the DataFrame for math scores by grade
print("Math Scores by Grade:")
print(math_scores_by_grade)

# Save the math scores by grade DataFrame as a CSV file
math_scores_by_grade.to_csv(r'C:\Users\Horva\Downloads\Starter_Code (6)\Starter_Code\PyCitySchools\Resources\math_scores_by_grade.csv', index=True)


# In[ ]:


# In[6]:


#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Read the student data CSV file
student_data = pd.read_csv(r'C:\Users\Horva\Downloads\Starter_Code (6)\Starter_Code\PyCitySchools\Resources\students_complete.csv')

# Pivot the student_data DataFrame to calculate the average reading score for each grade and school
reading_scores_by_grade = student_data.pivot_table(values='reading_score', index='school_name', columns='grade', aggfunc='mean')

# Display the DataFrame for reading scores by grade
print("Reading Scores by Grade:")
print(reading_scores_by_grade)

# Save the reading scores by grade DataFrame as a CSV file
reading_scores_by_grade.to_csv(r'C:\Users\Horva\Downloads\Starter_Code (6)\Starter_Code\PyCitySchools\Resources\reading_scores_by_grade.csv', index=True)


# In[ ]:


# In[7]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the school summary data
school_summary = pd.read_csv(r'C:\Users\Horva\Downloads\Starter_Code (6)\Starter_Code\PyCitySchools\Resources\school_summary.csv')

# Define the spending bins and labels
spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"]

# Categorize the spending per student using pd.cut
school_summary['Spending Ranges (Per Student)'] = pd.cut(school_summary['Per Student Budget'], bins=spending_bins, labels=labels)

# Calculate the mean scores per spending range
spending_math_scores = school_summary.groupby(["Spending Ranges (Per Student)"])["Average Math Score"].mean()
spending_reading_scores = school_summary.groupby(["Spending Ranges (Per Student)"])["Average Reading Score"].mean()
spending_passing_math = school_summary.groupby(["Spending Ranges (Per Student)"])["% Passing Math"].mean()
spending_passing_reading = school_summary.groupby(["Spending Ranges (Per Student)"])["% Passing Reading"].mean()
overall_passing_spending = school_summary.groupby(["Spending Ranges (Per Student)"])["% Overall Passing"].mean()

# Create the spending_summary DataFrame
spending_summary = pd.DataFrame({
    "Average Math Score": spending_math_scores,
    "Average Reading Score": spending_reading_scores,
    "% Passing Math": spending_passing_math,
    "% Passing Reading": spending_passing_reading,
    "% Overall Passing": overall_passing_spending
})

# Display the spending_summary DataFrame
print("Spending Summary:")
print(spending_summary)


# In[ ]:


# In[8]:


#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

# Load the per_school_summary DataFrame
per_school_summary = pd.read_csv(r'C:\Users\Horva\Downloads\Starter_Code (6)\Starter_Code\PyCitySchools\Resources\school_summary.csv')

# Define the size bins and labels
size_bins = [0, 1000, 2000, 5000]
labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

# Create a new column in per_school_summary for school size
per_school_summary['School Size'] = pd.cut(per_school_summary['Total Students'], bins=size_bins, labels=labels)

# Calculate the mean scores and passing percentages for each size category
size_math_scores = per_school_summary.groupby('School Size')['Average Math Score'].mean()
size_reading_scores = per_school_summary.groupby('School Size')['Average Reading Score'].mean()
size_passing_math = per_school_summary.groupby('School Size')['% Passing Math'].mean()
size_passing_reading = per_school_summary.groupby('School Size')['% Passing Reading'].mean()
size_overall_passing = per_school_summary.groupby('School Size')['% Overall Passing'].mean()

# Create the size_summary DataFrame
size_summary = pd.DataFrame({
    'Average Math Score': size_math_scores,
    'Average Reading Score': size_reading_scores,
    '% Passing Math': size_passing_math,
    '% Passing Reading': size_passing_reading,
    '% Overall Passing': size_overall_passing
})

# Display the size_summary DataFrame
print("Size Summary:")
print(size_summary)

# Save the size_summary DataFrame as a CSV file
size_summary.to_csv(r'C:\Users\Horva\Downloads\Starter_Code (6)\Starter_Code\PyCitySchools\Resources\size_summary.csv', index=False)


# In[ ]:


# In[9]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Read the per_school_summary.csv file
per_school_summary = pd.read_csv('C:/Users/Horva/Downloads/per_school_summary.csv')

# Group the per_school_summary DataFrame by "Total Students"
type_summary = per_school_summary.groupby('Total Students').mean()

# Display the type_summary DataFrame
print("Scores by School Type:")
print(type_summary)



# In[ ]:




