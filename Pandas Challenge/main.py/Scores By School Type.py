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




