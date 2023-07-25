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




