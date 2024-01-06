#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 23:57:18 2024

@author: zhihaowang
"""

import pandas as pd
import yfinance as yf
from datetime import datetime

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

aapl_data = yf.download('AAPL', start=start_date, end=end_date)
msft_data = yf.download('MSFT', start=start_date, end=end_date)

# print(aapl_data.head())
# print(msft_data.head())
# print(aapl_data.tail())
# print(msft_data.tail())

# View summary statistics
print("\nSummary statistics for AAPL data:")
print(aapl_data.describe())

# Check data types and index
print("\nData types and index for AAPL data:")
print(aapl_data.info())

# Calculate daily returns for AAPL
aapl_data['Daily Return'] = (aapl_data['Close'] - aapl_data['Close'].shift(1)) / aapl_data['Close'].shift(1)

# Calculate daily returns for MSFT
msft_data['Daily Return'] = (msft_data['Close'] - msft_data['Close'].shift(1)) / msft_data['Close'].shift(1)

# Display the first few rows of the updated DataFrame
print("AAPL data with daily returns:")
print(aapl_data.head())

print("\nMSFT data with daily returns:")
print(msft_data.head())

import matplotlib.pyplot as plt

# Plotting stock prices
plt.figure(figsize=(10, 5))
plt.plot(aapl_data['Close'], label='AAPL')
plt.plot(msft_data['Close'], label='MSFT')
plt.title('Closing Price of AAPL and MSFT Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)
plt.show()

# Plotting daily returns
plt.figure(figsize=(10, 5))
plt.plot(aapl_data['Daily Return'], label='AAPL Daily Return')
plt.plot(msft_data['Daily Return'], label='MSFT Daily Return')
plt.title('Daily Return of AAPL and MSFT')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.legend()
plt.grid(True)
plt.show()

# Moving Averages
aapl_data['20-Day MA'] = aapl_data['Close'].rolling(window=20).mean()
aapl_data['50-Day MA'] = aapl_data['Close'].rolling(window=50).mean()

plt.figure(figsize=(10, 5))
plt.plot(aapl_data['Close'], label='AAPL Closing Price')
plt.plot(aapl_data['20-Day MA'], label='20-Day MA')
plt.plot(aapl_data['50-Day MA'], label='50-day MA')
plt.title('AAPL Closing Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Comparative Histogram
plt.figure(figsize=(10, 5))
plt.hist(aapl_data['Daily Return'].dropna(), bins=50, alpha=0.5, label='AAPL')
plt.hist(msft_data['Daily Return'].dropna(), bins=50, alpha=0.5, label='MSFT')
plt.title('Comparison of Daily Return: AAPL vs MSFT')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# box plots, scatter plots, etc.) to analyze different aspects of the stock data.

