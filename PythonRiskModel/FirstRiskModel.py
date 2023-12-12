import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Function to download historical stock prices
def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data['Adj Close']

# Function to calculate daily returns
def calculate_daily_returns(stock_prices):
    # stock_prices is a pandas DataFrame or Series
    '''
    pct_change:
    is a pandas method applied to a Series that calculates the percentage 
    change between the current and a prior element
    '''
    
    '''
    dropna():
    After calculating the percentage changes, there might be NaN (Not a Number) values 
    in the resulting Series or DataFrame, especially for the first row where there is 
    no prior element to calculate the percentage change. The .dropna() method is used 
    to remove those NaN values, ensuring that you are left with a clean set of daily 
    returns without missing values.
    '''
    return stock_prices.pct_change().dropna()

# Function to calculate Value at Risk (VaR)
def calculate_var(returns, confidence_level=0.95):
    '''
    returns: This is assumed to be a NumPy array or a pandas Series containing 
    the historical returns of a financial instrument or portfolio.
    '''
    
    '''
    confidence interval https://www.youtube.com/watch?v=ENnlSlvQHO0
    value at risk: https://corporatefinanceinstitute.com/resources/career-map/sell-side/risk-management/value-at-risk-var/?campaignid=17756089871&adgroupid=&adid=&gad_source=2&gclid=CjwKCAiAvdCrBhBREiwAX6-6UnLIStv7k_RfkgrpOEghEj6jmzs9XZdI5ynOqG6mMhQ3pXNcEx47zBoCsYIQAvD_BwE
    monte carlo simulation 
    '''
    return np.percentile(returns, 100 * (1 - confidence_level))


# Function to plot the results
def plot_risk_model(returns, var):
    plt.figure(figsize=(10, 6))
    returns.plot(label='Daily Returns')
    plt.axhline(-var, color='r', linestyle='--', label='VaR at 95% confidence')
    plt.title('Risk Model: Value at Risk (VaR)')
    plt.legend()
    plt.show()
    
# Define parameters
ticker = 'DADA'
start_date = '2023-01-01'
end_date = '2023-12-08'
confidence_level = 0.95

# Download historical stock prices
stock_prices = get_stock_data(ticker, start_date, end_date)

# Calculate daily returns
returns = calculate_daily_returns(stock_prices)

# Calculate Value at Risk (VaR)
var = calculate_var(returns, confidence_level)
    
# Plot the risk model
plot_risk_model(returns, var)
