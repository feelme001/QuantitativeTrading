#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 23:03:02 2023

@author: zhihaowang
"""

# Merging and Concatenating DataFrames

# pandas_merge_concat.py
import pandas as pd


# Create two sample DataFrames
df1 = pd.DataFrame({
    'ID' : [1,2,3],
    'Name': ['Alice', 'Bob', 'Charlie']})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Age': [25, 30, 35]})

# Display the original DataFrames
print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

# Merge DataFrames based on a common column (ID)
merged_df = pd.merge(df1, df2, on='ID', how='inner')

# Display the merged DataFrame
# if df1 has record, but df2 does not, remove that record, same for df2
# only join on data that both table have that record
print("\nMerged DataFrame:")
print(merged_df)

# Concatenate DataFrames along rows
concatenated_df = pd.concat([df1, df2], ignore_index=True)

# Display the concatenated DataFrame
print("\nConcatenated DataFrame:")
print(concatenated_df)


# Create sample data for data1.csv
data1 = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 75000]
}

df1 = pd.DataFrame(data1)
df1.to_csv('data1.csv', index=False)

# Create sample data for data2.csv
data2 = {
    'ID': [2, 3, 4],
    'City': ['New York', 'San Francisco', 'Los Angeles'],
    'Salary': [55000, 70000, 80000]
}

df2 = pd.DataFrame(data2)
df2.to_csv('data2.csv', index=False)

print("##############################")
# Read sample DataFrames from CSV files
df1_read = pd.read_csv('data1.csv')
df2_read = pd.read_csv('data2.csv')

# Display the original DataFrames
print("DataFrame 1:")
print(df1_read)

print("\nDataFrame 2:")
print(df2_read)

# Merge DataFrames based on a common column (ID)
merged_df = pd.merge(df1_read, df2_read, on='ID', how='inner')
# Display the merged DataFrame
print("\nMerged DataFrame:")
print(merged_df)
merged_df.to_csv('data1_data2_merged.csv', index=False)

# Concatenate DataFrames along rows
concatenated_df = pd.concat([df1_read, df2_read], ignore_index=True)

# Display the concatenated DataFrame
print("\nConcatenated DataFrame:")
print(concatenated_df)
concatenated_df.to_csv('data1_data2_concatenated.csv', index=False)


