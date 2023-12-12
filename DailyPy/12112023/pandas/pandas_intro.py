#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 21:15:02 2023

@author: zhihaowang
"""

import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

print("DataFram:")
print(df)

# Accessing columns
print("\nAccessing 'Name' column:")
print(df['Name'])

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Adding a new column
df['Occupation'] = ['Engineer', 'Teacher', 'Doctor']

print("\nUpdated DataFrame:")
print(df)

# Read CSV into DataFrame
df = pd.read_csv('sample_data.csv')

# Displaying the DataFrame
print("Original DataFrame:")
print(df)

# Filtering rows
filtered_df = df[df['Age'] > 25]

# Calculating summary statistics
stats = df.describe()

filtered_df.to_csv('filtered_data.csv', index=False)
stats.to_csv('summary_statistics.csv')

print("\nFiltered DataFrame:")
print(filtered_df)
print("\nSummary Statistics:")
print(stats)