import yfinance as yf
import pandas as pd

# List of S&P 500 tickers (explicitly listed)
sp500_tickers = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'TSLA', 'META', 'BRK-B', 'V', 'JNJ', 
    'WMT', 'UNH', 'HD', 'PG', 'MA', 'PYPL', 'DIS', 'VZ', 'NFLX', 'KO', 'INTC', 
    'CSCO', 'PEP', 'MRK', 'ADM', 'ABT', 'XOM', 'CVX', 'T', 'GE', 'IBM', 'ORCL', 
    'LLY', 'PFE', 'BA', 'BA', 'MMM', 'GS', 'UPS', 'MCD', 'CAT', 'SPGI', 'AMGN', 
    'SCHW', 'LMT', 'INTU', 'COP', 'MS', 'SBUX', 'RTX', 'ISRG', 'TMO', 'BMY', 
    'AXP', 'AMT', 'ZTS', 'COST', 'BLK', 'SPG', 'WFC', 'BAX', 'MDT', 'CCI', 'AON', 
    'ICE', 'SYK', 'APD', 'TROW', 'CME', 'MSCI', 'DE', 'ADBE', 'AIG', 'TGT', 'FIS', 
    'EVRG', 'DHR', 'DOW', 'HUM', 'CSX', 'NKE', 'FISV', 'VLO', 'ETN', 'XEL', 'LUV', 
    'LNC', 'CSX', 'PFE', 'BAX', 'V', 'MDT', 'MMM', 'WBA', 'MNST', 'TXN', 'AMAT', 'ZS', 'CRM', 'PSTG'
]

# Get fair value estimate (target price) and current price from Yahoo Finance
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    try:
        fair_value = stock.info.get('targetMeanPrice')  # Target price estimate
        current_price = stock.info.get('currentPrice')  # Current market price
        return fair_value, current_price
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None, None

# Main function to fetch fair value estimates for all S&P 500 companies
def main():
    results = []

    # Loop through each ticker and fetch the fair value estimate and current price
    for ticker in sp500_tickers:
        print(f"Processing ticker: {ticker}...")
        
        fair_value_estimate, current_price = get_stock_data(ticker)
        
        if fair_value_estimate is None or current_price is None:
            undervalued = 'Error'
            percent_variance = 'N/A'
        else:
            # Determine if the stock is undervalued (fair value > current price)
            undervalued = 'Yes' if fair_value_estimate > current_price else 'No'
            
            # Calculate the percentage variance between fair value and current price
            percent_variance = ((fair_value_estimate - current_price) / current_price) * 100
        
        results.append({
            'Ticker': ticker,
            'Fair Value Estimate': fair_value_estimate if fair_value_estimate is not None else 'N/A',
            'Current Price': current_price if current_price is not None else 'N/A',
            'Undervalued': undervalued,
            'Percentage Variance': percent_variance if isinstance(percent_variance, str) else round(percent_variance, 2)  # rounding to 2 decimal places
        })
    
    # Convert results into a pandas DataFrame
    df = pd.DataFrame(results)

    # Output results to an Excel file (use raw string literal for path)
    output_file = r'C:\Users\mjlem\OneDrive\Desktop\python_work\sp500_fair_value_estimates.xlsx'
    df.to_excel(output_file, index=False)

    print(f"Data saved to {output_file}")

# Run the main function
if __name__ == "__main__":
    main()

