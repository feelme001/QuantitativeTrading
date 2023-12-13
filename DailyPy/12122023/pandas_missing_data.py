#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 00:40:00 2023

@author: zhihaowang
"""

# pandas_missing_data.py
import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [10, np.nan, 30, np.nan, 50],
    'C': [100, 200, 300, 400, 500]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing Values:")
print(missing_values)

# Drop rows with missing values
df_dropped = df.dropna()

# Display the DataFrame after dropping missing values
print("\nDataFrame after dropping missing values:")
print(df_dropped)

# Fill missing values with a specified value (e.g., mean)
df_filled = df.fillna(df.mean())

# Display the DataFrame after filling missing values
print("\nDataFrame after filling missing values:")
print(df_filled)

df.to_csv('sample_data_missing_data.csv', index=False)

df_read = pd.read_csv('sample_data_missing_data.csv')

print(df_read)
df_read_fill = df_read.fillna(df.mean())
print(df_read_fill)

analysis_result = df_filled.describe()
print("\nDescriptive Statistics:")
print(analysis_result)


