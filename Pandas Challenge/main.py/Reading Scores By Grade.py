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




