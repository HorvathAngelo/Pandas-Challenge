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




