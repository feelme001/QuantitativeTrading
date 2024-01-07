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
end_date = datetime(2023, 12, 31)

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
