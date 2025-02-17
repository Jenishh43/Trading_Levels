import yfinance as yf
import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
import mplfinance as mpf

def fetch_Data(ticker, period = "1mo" , accuracy = 5):
    
    data = yf.download(ticker, interval="1h", period=period, multi_level_index=False)

    filtered_data = data[['High', 'Low']]

    accuracy = int(accuracy)
    
    resistance_level = filtered_data.iloc[argrelextrema(filtered_data['High'].values, np.greater_equal, order=accuracy)[0]]['High'].values
    
    support_level = filtered_data.iloc[argrelextrema(filtered_data['Low'].values, np.less_equal, order=accuracy)[0]]['Low'].values

    return data, resistance_level, support_level