#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 21:36:39 2024

@author: zhihaowang
"""

'''
1. Study Different Types of Risks:
    
Market Risk: This is the risk of losses due to factors that affect the overall performance of the financial markets.

Credit Risk: The risk of loss due to a borrower's inability to make payments as agreed.

Liquidity Risk: The risk that an asset cannot be traded quickly enough in the market to prevent a loss (or make the required profit).

Operational Risk: Risks arising from execution of a company’s business functions.

Systematic and Unsystematic Risk: Systematic risk is inherent to the entire market or market segment, while unsystematic risk is unique to a specific company or industry.

Interest Rate Risk, Currency Risk, and others: Depending on the focus of the portfolio, these risks may also be relevant.
'''

'''
2. Understand the Importance of Risk Management:
- Risk management is about identifying, assessing, and prioritizing risks followed by 
coordinated application of resources to minimize, control, and monitor the impact o
f unfortunate events or to maximize the realization of opportunities.

- Good risk management can help avoid large losses and improve the performance 
consistency of your portfolio.  
'''

'''
3. Explore Basic Risk Mitigation Techniques:
Asset Allocation and Diversification: 
Asset Allocation: This involves spreading investments across various asset classes (like stocks, bonds, real estate, commodities) to balance the risk and return in a portfolio. The idea is that different asset classes respond differently to the same economic event, so when one asset class is underperforming, another might be performing well, thereby reducing overall risk.
Diversification: This is the practice of spreading investments within an asset class. For example, instead of investing in a single stock or sector, you invest in a range of stocks across various sectors. Diversification reduces unsystematic risk, which is the risk specific to an individual asset or sector.



Hedging: 
Hedging involves taking an offsetting position in a related security, such as options or futures contracts, to mitigate the risk of adverse price movements in an asset. For example, if you own a stock, you might buy a put option on the same stock, which increases in value if the stock price falls, offsetting the loss.

Position Sizing:
Position Sizing is the process of determining how much of your portfolio to allocate to a particular investment. By limiting the amount invested in any one asset, you can manage the potential loss it can cause to your overall portfolio. It's a way to control risk by not "putting all your eggs in one basket."

Using Stop-Loss Orders and Derivatives:
Stop-Loss Orders: A stop-loss order is an order placed with a broker to buy or sell a security when it reaches a certain price. It's designed to limit an investor's loss on a security position. For example, setting a stop-loss order for 10% below the price at which you bought the stock will limit your loss to 10%.
Derivatives: Financial instruments like options and futures can be used to hedge against various risks. For example, options can provide insurance against price movements in the underlying asset, while futures contracts can lock in prices for future transactions.
    
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # For heatmap visualization

import yfinance as yf
stocks = ['AAPL', 'MSFT', 'GOOG', 'AMZN']  # Example stock tickers
data = yf.download(stocks, start='2020-01-01', end='2021-01-01')['Adj Close']

daily_returns = data.pct_change().dropna()

correlation_matrix = daily_returns.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix for Portfolio Assets')
plt.show()

