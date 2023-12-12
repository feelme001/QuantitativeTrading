#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 21:46:41 2023

@author: zhihaowang
"""

import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Displaying the DataFrame
print("Original DataFrame:")
print(df)

# Filtering rows based on a condition
filtered_df = df[df['Age'] > 25]

# Sorting the DataFrame by a column
sorted_df = df.sort_values(by='Age', ascending=False)

new_row = pd.DataFrame({'Name': ['David'], 'Age': [28], 'City': ['Chicago']})
df = pd.concat([df, new_row], ignore_index=True)

# Grouping by a column and calculating aggregate statistics
grouped_df = df.groupby('City').agg({'Age': ['mean', 'min', 'max']}).reset_index()

# Displaying the results
print("\nFiltered DataFrame:")
print(filtered_df)

print("\nSorted DataFrame:")
print(sorted_df)

print("\nDataFrame with New Row:")
print(df)

print("\nGrouped DataFrame:")
print(grouped_df)