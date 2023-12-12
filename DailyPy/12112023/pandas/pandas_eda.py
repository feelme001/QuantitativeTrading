#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 22:18:09 2023

@author: zhihaowang
"""

import pandas as pd

# Task: Create a program that reads a CSV file into a Pandas DataFrame, 
# cleans the data, and performs exploratory data analysis (EDA).

# Read CSV into DataFrame
df = pd.read_csv('sample_data_1.csv')

# Display basic information about the DataFrame
print("Basic Information:")
print(df.info())
print(df)

# Handle missing values (replace NaN with the mean)
df_cleaned = df.apply(lambda x: x.fillna(x.mean()) if x.dtype.kind in 'biufc' else x)

# Display basic statistics of the cleaned DataFrame
print("\nBasic Statistics (Cleaned):")
print(df_cleaned.describe())
print(df_cleaned)
print(df.info())
print(df_cleaned.info())

"""
The lambda      x: x.fillna(x.mean()) if x.dtype.kind in 'biufc' else x 
function checks if the column type is numeric 
('biufc' includes integer, boolean, float, and complex). 
If it is, missing values are filled with the mean; 
otherwise, the column remains unchanged.

In NumPy and Pandas, 
the data type 'b' represents boolean values, 
and 'i', 'u', 'f', and 'c' represent integer, unsigned integer, float, and complex types, respectively.
"""

# check how many null in each column
df_cleaned.isnull().sum()

# Filling will only fill numical value, not filling boolean

