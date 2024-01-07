#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 09:56:31 2024

@author: zhihaowang
"""

import pandas as pd
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 1, 7)

aapl_data = yf.download('AAPL', start=start_date, end=end_date)
msft_data = yf.download('MSFT', start=start_date, end=end_date)

# Calculate daily returns for AAPL
aapl_data['Daily Return'] = (aapl_data['Close'] - aapl_data['Close'].shift(1)) / aapl_data['Close'].shift(1)

# Calculate daily returns for MSFT
msft_data['Daily Return'] = (msft_data['Close'] - msft_data['Close'].shift(1)) / msft_data['Close'].shift(1)

# Ensure x and y have the same length by dropping NaN values from the entire DataFrame
aapl_data = aapl_data.dropna(subset=['Daily Return', 'Volume'])
msft_data = msft_data.dropna(subset=['Daily Return', 'Volume'])


'''
# Additional stocks
additional_stocks = ['AMZN', 'GOOGL']  # Add more symbols as needed

# Fetch data for the additional stocks

for stock in additional_stocks:
    globals()[f"{stock.lower()}_data"] = yf.download(stock, start=start_date, end=end_date)
    
# Example for AMZN and GOOGL
print("AMZN data:")
print(amzn_data.head())
print(amzn_data.describe())

print("\nGOOGL data:")
print(googl_data.head())
print(googl_data.describe())

variable_names = ['amzn_data', 'googl_data']  # List of variables to delete

for var in variable_names:
    if var in globals():
        del globals()[var]

'''

# Define the stocks you want to fetch
additional_stocks = ['AMZN', 'GOOGL']  # Add more symbols as needed

# Create a dictionary to store stock data
stock_data = {}

# Fetch data for each stock and store it in the dictionary
for stock in additional_stocks:
    stock_data[stock] = yf.download(stock, start='2023-01-01', end='2023-12-31')

# Accessing data for a specific stock
amzn_data = stock_data['AMZN']
googl_data = stock_data['GOOGL']

# Calculate daily returns for AMZN
amzn_data['Daily Return'] = (amzn_data['Close'] - amzn_data['Close'].shift(1)) / amzn_data['Close'].shift(1)

# Calculate daily returns for GOOGL
googl_data['Daily Return'] = (googl_data['Close'] - googl_data['Close'].shift(1)) / googl_data['Close'].shift(1)

amzn_data = amzn_data.dropna(subset=['Daily Return', 'Volume'])
googl_data = googl_data.dropna(subset=['Daily Return', 'Volume'])


aapl_data['Cumulative Return'] = (1 + aapl_data['Daily Return']).cumprod() - 1
msft_data['Cumulative Return'] = (1 + msft_data['Daily Return']).cumprod() - 1
amzn_data['Cumulative Return'] = (1 + amzn_data['Daily Return']).cumprod() - 1
googl_data['Cumulative Return'] = (1 + googl_data['Daily Return']).cumprod() - 1

print("AAPL data:")
print(aapl_data.head())
print(aapl_data.tail())
print(aapl_data.describe())

print("MSFT data:")
print(msft_data.head())
print(msft_data.tail())
print(msft_data.describe())


# Example for AMZN and GOOGL
print("AMZN data:")
print(amzn_data.head())
print(amzn_data.tail())
print(amzn_data.describe())

print("\nGOOGL data:")
print(googl_data.head())
print(googl_data.tail())
print(googl_data.describe())

plt.figure(figsize=(10, 6))

plt.plot(aapl_data.index, aapl_data['Cumulative Return'], label='AAPL')
plt.plot(msft_data.index, msft_data['Cumulative Return'], label='MSFT')
plt.plot(amzn_data.index, amzn_data['Cumulative Return'], label='AMZN')
plt.plot(googl_data.index, googl_data['Cumulative Return'], label='GOOGL')

plt.title('Cumulative Returns of AAPL, MSFT, AMZN, GOOGL')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend()
plt.grid(True)
plt.show()

'''
Analysis and Interpretation:
Look for Trends: Identify any clear trends in the data. For example, did all stocks react similarly to market events?
- All 4 stocks are trending up

Performance Comparison: Determine which stocks had the highest and lowest cumulative returns over the period.
- Amazon has the highest and Apple has the lowest cumulative returns over the period 

Volatility Insights: Notice periods of high volatility. These are typically represented by steeper slopes (upward or downward) in the cumulative return curve.
- 
'''

# Calculate Average Daily Returns
aapl_avg_daily_return = aapl_data['Daily Return'].mean()
msft_avg_daily_return = msft_data['Daily Return'].mean()
amzn_avg_daily_return = amzn_data['Daily Return'].mean()
googl_avg_daily_return = googl_data['Daily Return'].mean()

# Calculate Volatility (Standard Deviation)
aapl_volatility = aapl_data['Daily Return'].std()
msft_volatility = msft_data['Daily Return'].std()
amzn_volatility = amzn_data['Daily Return'].std()
googl_volatility = googl_data['Daily Return'].std()

plt.figure(figsize=(10, 6))
# Plot each stock as a point in the scatter plot
plt.scatter(aapl_volatility, aapl_avg_daily_return, label='AAPL')
plt.scatter(msft_volatility, msft_avg_daily_return, label='MSFT')
plt.scatter(amzn_volatility, amzn_avg_daily_return, label='AMZN')
plt.scatter(googl_volatility, googl_avg_daily_return, label='GOOGL')

plt.title('Risk vs. Return of stocks')
plt.xlabel('Volatility (Standard Deviation of Daily Returns)')
plt.ylabel('Average Daily Return')
plt.legend()
plt.grid(True)
plt.show()

# Create a new DataFrame for daily returns
daily_returns = pd.DataFrame({
    'AAPL': aapl_data['Daily Return'],
    'MSFT': msft_data['Daily Return'],
    'AMZN': amzn_data['Daily Return'],
    'GOOGL': googl_data['Daily Return']
    })

# Calculate the correlation matrix
corr_matrix = daily_returns.corr()

# Display the correlation matrix
print(corr_matrix)

import seaborn as sns

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Metrix Heatmap')
plt.show()

import mplfinance as mpf
# Example for AAPL
mpf.plot(aapl_data, type='candle', mav=(20, 50), volume=True, show_nontrading=True)

plt.fill_between(aapl_data.index, aapl_data['Cumulative Return'], label='AAPL', alpha=0.5)
plt.fill_between(msft_data.index, msft_data['Cumulative Return'], label='MSFT', alpha=0.5)
plt.title('Cumulative Returns of AAPL and MSFT')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend()
plt.show()


plt.hist(aapl_data['Daily Return'].dropna(), bins=50, alpha=0.5, label='AAPL')
plt.hist(msft_data['Daily Return'].dropna(), bins=50, alpha=0.5, label='MSFT')
plt.title('Distribution of Daily Returns for AAPL and MSFT')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.legend()
plt.show()

'''
Candlestick Chart: Look for patterns like bullish or bearish trends, gaps, or reversals.

Area Charts: Understand the overall growth trajectory of each stock.

Histograms: Assess the normality of returns distribution, identify outliers, and compare the volatility of different stocks.
'''