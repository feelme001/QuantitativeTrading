#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 00:07:51 2023

@author: zhihaowang
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample DataFrame with random data
data = {
        'Category': ['A', 'B', 'C', 'D'],
        'Value': [25, 40, 30, 35]
        }

df = pd.DataFrame(data)

# Plot a simple bar chart
plt.bar(df['Category'], df['Value'])
plt.title('Simple Bar Chart')
plt.xlabel('category')
plt.ylabel('value')
plt.show()

# Create a sample time-series DataFrame
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
data = {
        'Date': date_rng,
        'Value': np.random.randint(1, 100, size=(len(date_rng)))
        }
df_time_series = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df_time_series.to_csv('sample_time_series_data.csv', index=False)

df_time_series_read = pd.read_csv('sample_time_series_data.csv', parse_dates=['Date'])

plt.plot(df_time_series_read['Date'], df_time_series_read['Value'])
plt.title('Time-Series Chart')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()