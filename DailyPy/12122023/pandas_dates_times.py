#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:43:04 2023

@author: zhihaowang
"""
import pandas as pd
import numpy as np

# Create a sample DataFrame with dates and times
date_rng = pd.date_range(start='2023-01-01', end='2023-01-05', freq='D')
df_dates = pd.DataFrame(date_rng, columns=['date'])

# Display the original DataFrame
print("Original DataFrame:")
print(df_dates)

# Extract components of the date (year, month, day, weekday)
df_dates['year'] = df_dates['date'].dt.year
df_dates['month'] = df_dates['date'].dt.month
df_dates['day'] = df_dates['date'].dt.day
df_dates['weekday'] = df_dates['date'].dt.day_name()

# Display the DataFrame with extracted date components
print("\nDataFrame with Extracted Date Components:")
print(df_dates)

# Create a sample time-series DataFrame
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
data = {
    'Date': date_rng,
    'Value': np.random.randint(1, 100, size=(len(date_rng)))
}

df_time_series = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df_time_series.to_csv('time_series_data.csv', index=False)

df_time_series = pd.read_csv('time_series_data.csv', parse_dates=['Date'])

# Display the original DataFrame
print("Original DataFrame:")
print(df_time_series)

# Extract components of the date (year, month, day, weekday)
df_time_series['year'] = df_time_series['Date'].dt.year
df_time_series['month'] = df_time_series['Date'].dt.month
df_time_series['day'] = df_time_series['Date'].dt.day
df_time_series['weekday'] = df_time_series['Date'].dt.day_name()

# Display the DataFrame with extracted date components
print("\nDataFrame with Extracted Date Components:")
print(df_time_series)