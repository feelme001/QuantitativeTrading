#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 00:17:48 2023

@author: zhihaowang
"""

# pandas_statistical_analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
        'Value': np.random.randint(1, 100, size=100)
        }

df = pd.DataFrame(data)

# Display basic statistics of the DataFrame
print("Basic Statistics:")
print(df.describe())

# Calculate the mean, median, and standard deviation
mean_value = df['Value'].mean()
median_value = df['Value'].median()
std_deviation = df['Value'].std()

print("\nMean Value:", mean_value)
print("Median Value:", median_value)
print("Standard Deviation:", std_deviation)

# Calculate the correlation matrix
correlation_metrix = df.corr()

print("\nCorrelation Matrix:")
print(correlation_metrix)

data2 = {
        'Value1': np.random.randint(1, 100, size=100),
        'Value2': np.random.randint(1, 100, size=100)
        }

df2 = pd.DataFrame(data2)
correlation_metrix2 = df2.corr()
print("\nCorrelation Matrix2:")
print(correlation_metrix2)

print(df)
df.to_csv('sample_data_one_value.csv', index=False)

df_read = pd.read_csv('sample_data_one_value.csv')
# Display basic statistics of the DataFrame
print("Basic Statistics:")
print(df_read.describe())
# Calculate the mean, median, and standard deviation
mean_value = df_read['Value'].mean()
median_value = df_read['Value'].median()
std_deviation = df_read['Value'].std()
print("\nMean Value:", mean_value)
print("Median Value:", median_value)
print("Standard Deviation:", std_deviation)

# Visualize the data with a histogram and box plot
plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
sns.histplot(df_read['Value'], bins=10, kde=True)
plt.title('Histogram')

plt.subplot(1,2,2)
sns.boxplot(y=df_read['Value'])
plt.title('Box Plot')
plt.show()




