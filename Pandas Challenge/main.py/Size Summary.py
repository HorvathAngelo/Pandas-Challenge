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




