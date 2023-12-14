#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 00:10:46 2023

@author: zhihaowang
"""

import pandas as pd

# 1. Creating Date Columns:

# Creating a DataFrame with a date column
data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-03']}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Extracting components of a date
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

print(df)

# 2. Date Arithmetic:

# Adding a number of days to a date column
df['Date_Plus_7_Days'] = df['Date'] + pd.to_timedelta(7, unit='D')

# Calculating the difference between two date columns
df['Date_Diff'] = df['Date_Plus_7_Days'] - df['Date']

print(df)

# 3. Filtering by Date:

# Filtering rows based on a date range
start_date = '2023-01-02'
end_date = '2023-01-03'
filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
print(filtered_df)

# NumPy
import numpy as np

# 1. Generating Date Ranges:
# Generating a date range using NumPy
date_range = pd.date_range(start='2023-01-01', end='2023-01-05')
print(date_range)
# 2. Working with Timedeltas:
# Calculating the difference between two dates
date1 = pd.to_datetime('2023-01-01')
date2 = pd.to_datetime('2023-01-05')
date_diff = date2 - date1

# Converting timedelta to days
days_diff = date_diff / np.timedelta64(1, 'D')
print(days_diff)
