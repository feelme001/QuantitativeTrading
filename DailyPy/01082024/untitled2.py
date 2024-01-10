#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 21:35:51 2024

@author: zhihaowang
"""

# Efficient frontier

import yfinance as yf
import pandas as pd
import numpy as np

# Define the stocks and time period
stocks = ['AAPL', 'MSFT', 'AMZN', 'GOOGL']
start = '2023-01-01'
end = '2024-01-01'

# Fetch historical data
data = yf.download(stocks, start=start, end=end)['Adj Close']

returns = data.pct_change().dropna()

print(returns.head())

np.random.seed(42)
num_portfolios = 10000
all_weights = np.zeros((num_portfolios, len(stocks)))
ret_arr = np.zeros(num_portfolios)
vol_arr = np.zeros(num_portfolios)
sharpe_arr = np.zeros(num_portfolios)

for i in range(num_portfolios):
    # Create random weight
    weights = np.array(np.random.random(len(stocks)))
    weights = weights / np.sum(weights)
    
    # Save weights
    all_weights[i, :] = weights
    
    # Expected return
    ret_arr[i] = np.sum((returns.mean() * weights * 252))
    
    # Expected volatility
    vol_arr[i] = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    
    # Sharpe Ratio
    sharpe_arr[i] = ret_arr[i] / vol_arr[i]
    
max_sharpe_ratio = sharpe_arr.max()
max_sharpe_ratio_idx = sharpe_arr.argmax()
max_sharpe_portfolio = all_weights[max_sharpe_ratio_idx,:]

print("Portfolio with the highest Sharpe Ratio:")
print("Stock Weights:", max_sharpe_portfolio)
print("Expected Annual Return:", ret_arr[max_sharpe_ratio_idx])
print("Annual Volatility:", vol_arr[max_sharpe_ratio_idx])

import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='viridis')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')

# Highlight the point with the highest Sharpe ratio
plt.scatter(vol_arr[max_sharpe_ratio_idx], ret_arr[max_sharpe_ratio_idx], c='red', s=50) 
plt.show()

# check