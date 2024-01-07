#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 17:29:02 2024

@author: zhihaowang
"""

import pandas as pd
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

aapl_data = yf.download('AAPL', start=start_date, end=end_date)
msft_data = yf.download('MSFT', start=start_date, end=end_date)

# Calculate daily returns for AAPL
aapl_data['Daily Return'] = (aapl_data['Close'] - aapl_data['Close'].shift(1)) / aapl_data['Close'].shift(1)

# Calculate daily returns for MSFT
msft_data['Daily Return'] = (msft_data['Close'] - msft_data['Close'].shift(1)) / msft_data['Close'].shift(1)

plt.figure(figsize=(10, 5))
plt.boxplot([aapl_data['Daily Return'].dropna(), msft_data['Daily Return'].dropna()], labels=['AAPL', 'MSFT'])
plt.title('Box Plot of Daily Returns for AAPL and MSFT')
plt.ylabel('Daily Return')
plt.show()

# Sample data: Daily Returns vs. Volume for AAPL
plt.scatter(aapl_data['Daily Return'], aapl_data['Volume'])

plt.title('AAPL Daily Returns vs. Trading Volume')
plt.xlabel('Daily Return')
plt.ylabel('Trading Volume')
plt.grid(True)
plt.show()

"""
Looks like a positive correlation that higher returns might correlate with higher trading volumes
"""


import numpy as np

# Ensure x and y have the same length by dropping NaN values from the entire DataFrame
aapl_filtered = aapl_data.dropna(subset=['Daily Return', 'Volume'])

# Use the filtered data for x and y
x = aapl_filtered['Daily Return']
y = aapl_filtered['Volume']

# Normalize the Volume data
y_normalized = y / y.max()

# Perform linear regression on the normalized data
slope, intercept = np.polyfit(x, y_normalized, 1)

# Create trend line data
trend_line = slope * x + intercept

# Plotting scatter plot with normalized Volume
plt.scatter(x, y_normalized)
plt.plot(x, trend_line, color='red', label='Trend Line')

plt.title('AAPL Daily Returns vs. Normalized Trading Volume')
plt.xlabel('Daily Return')
plt.ylabel('Normalized Volume')
plt.legend()
plt.show()



# Sample data
np.random.seed(0)
x = 2 - 3 * np.random.normal(0, 1, 20)
y = x - 2 * (x ** 2) + 1 * (x ** 3) + np.random.normal(-3, 3, 20)

# Polynomial Regression
coefficients_degree_3 = np.polyfit(x, y, 3)
polynomial_degree_3 = np.poly1d(coefficients_degree_3)
coefficients_degree_4 = np.polyfit(x, y, 4)
polynomial_degree_4 = np.poly1d(coefficients_degree_4)

# Plot
xp = np.linspace(-6, 3, 100)
plt.scatter(x, y)
plt.plot(xp, polynomial_degree_3(xp), 'r-', label='Degree 3')
plt.plot(xp, polynomial_degree_4(xp), 'b--', label='Degree 4')
plt.title('Polynomial Regression Examples')
plt.legend()
plt.show()





