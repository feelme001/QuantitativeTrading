#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 00:48:16 2023

@author: zhihaowang
"""

# pandas_group_aggregate.py
import pandas as pd

# Create a sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Group the DataFrame by 'Category' and calculate the mean of each group
grouped_df = df.groupby('Category').mean()

# Display the grouped DataFrame
print("\nGrouped DataFrame:")
print(grouped_df)

# Perform multiple aggregations on each group
aggregated_df = df.groupby('Category').agg({'Value': ['mean', 'sum', 'min', 'max']})

# Display the DataFrame with multiple aggregations
print("\nDataFrame with Multiple Aggregations:")
print(aggregated_df)