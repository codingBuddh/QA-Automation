import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from typing import List, Dict, Union
from app.config import settings

def get_stock_prices(
    stock_symbols: Union[str, List[str]], 
    start_date: datetime, 
    end_date: datetime
) -> pd.DataFrame:
    """Get the stock prices for the given stock symbols between the start and end dates."""
    if isinstance(stock_symbols, str):
        stock_symbols = [stock_symbols]
    
    stock_data = yf.download(stock_symbols, start=start_date, end=end_date)
    return stock_data.get("Close")

def plot_stock_prices(stock_prices: pd.DataFrame, filename: str) -> str:
    """Plot the stock prices and save to the specified filename."""
    plt.figure(figsize=(12, 6))
    
    for column in stock_prices.columns:
        normalized_prices = stock_prices[column] / stock_prices[column].iloc[0] * 100
        plt.plot(stock_prices.index, normalized_prices, label=column)
    
    plt.title("Stock Price Performance (Normalized)")
    plt.xlabel("Date")
    plt.ylabel("Price (%)")
    plt.grid(True)
    plt.legend()
    
    # Save to the plots directory
    filepath = settings.PLOT_FOLDER / filename
    plt.savefig(filepath)
    plt.close()
    
    return filename

def get_ytd_stock_data(symbols: List[str]) -> Dict:
    """Get year-to-date stock data for the given symbols."""
    start_date = datetime(datetime.now().year, 1, 1)
    end_date = datetime.now()
    
    prices = get_stock_prices(symbols, start_date, end_date)
    plot_filename = f"stock_prices_YTD_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    plot_path = plot_stock_prices(prices, plot_filename)
    
    # Calculate YTD returns
    ytd_returns = {
        symbol: ((prices[symbol].iloc[-1] / prices[symbol].iloc[0]) - 1) * 100
        for symbol in symbols
    }
    
    return {
        'plot_path': plot_path,
        'ytd_returns': ytd_returns,
        'last_updated': datetime.now()
    } 