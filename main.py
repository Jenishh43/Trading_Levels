import yfinance as yf
import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
import mplfinance as mpf
from tkinter import *

def fetch_Data(ticker, period = "1mo" , accuracy = 5):
    
    data = yf.download(ticker, interval="1h", period=period, multi_level_index=False)

    filtered_data = data[['High', 'Low']]

    accuracy = int(accuracy)
    
    resistance_level = filtered_data.iloc[argrelextrema(filtered_data['High'].values, np.greater_equal, order=accuracy)[0]]['High'].values
    
    support_level = filtered_data.iloc[argrelextrema(filtered_data['Low'].values, np.less_equal, order=accuracy)[0]]['Low'].values

    mpf.plot(data, type='candle', style='charles', title=f'{ticker} Candlestick Chart with Support/Resistance', ylabel='Price', ylabel_lower='Volume', volume=True, hlines=dict(hlines=list(resistance_level) + list(support_level), colors=['r']*len(resistance_level) + ['g']*len(support_level), linestyle='dashed'))

    return

def on_submit():
    ticker = ticker_entry.get()
    period = period_entry.get()
    accuracy = accuracy_entry.get()
    fetch_Data(ticker, period, accuracy)

root = Tk()
root.title("Stock Chart with Support/Resistance")

Label(root, text="Ticker:").grid(row=0, column=0)
ticker_entry = Entry(root)
ticker_entry.grid(row=0, column=1)

Label(root, text="Period:").grid(row=1, column=0)
period_entry = Entry(root)
period_entry.grid(row=1, column=1)

Label(root, text="Accuracy:").grid(row=2, column=0)
accuracy_entry = Entry(root)
accuracy_entry.grid(row=2, column=1)

Button(root, text="Fetch Data", command=on_submit).grid(row=3, columnspan=2)

root.mainloop()