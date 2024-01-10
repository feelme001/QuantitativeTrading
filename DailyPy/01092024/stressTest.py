#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 22:29:37 2024

@author: zhihaowang
"""

# Stress Test Scenarios

# Import necessary libraries
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Fetch historical data for a sample portfolio
stocks = ['AAPL', 'MSFT', 'TSLA', 'GOOGL', 'AMZN']
data = yf.download(stocks, start='2019-01-01', end='2021-01-01')['Adj Close']

# Calculate daily returns
daily_returns = data.pct_change().dropna()

# Define portfolio weights (example: equally weighted)
portfolio_weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])

# Stress Test: Market Downturn in March 2020
march_downturn = daily_returns['2020-03-01':'2020-04-01'].mean()
march_portfolio_impact = np.dot(portfolio_weights, march_downturn) * 252

# Scenario Analysis: Hypothetical Market Drop
# Assuming a 10% drop in stocks and a 5% increase in bonds (if any)
scenario_returns = daily_returns.mean() * np.array([0.9, 0.9, 0.9, 1.05, 1.05])
scenario_portfolio_impact = np.dot(portfolio_weights, scenario_returns) * 252

# Plotting the results
plt.figure(figsize=(8, 5))
plt.bar(['March 2020 Downturn', 'Hypothetical Scenario'], [march_portfolio_impact, scenario_portfolio_impact])
plt.ylabel('Annualized Portfolio Return')
plt.title('Portfolio Performance under Different Stress Tests')
plt.axhline(y=0, color='gray', linestyle='--')
plt.show()

