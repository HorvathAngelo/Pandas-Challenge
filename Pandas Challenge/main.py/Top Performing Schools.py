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




