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




