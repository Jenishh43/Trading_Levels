# Trading Levels Visualization Tool

This repository provides a tool to visualize stock trading levels using historical stock data from Yahoo Finance. The application plots candlestick charts along with support and resistance levels.

## Features
- Fetches historical stock data from Yahoo Finance.
- Plots candlestick charts using `mplfinance`.
- Identifies and displays support and resistance levels.
- Provides a simple GUI for user input using `Tkinter`.

## Dependencies
- `yfinance`
- `pandas`
- `numpy`
- `scipy`
- `mplfinance`
- `tkinter` (Standard Python library)

Install dependencies using:
```bash
pip install -r requiremens.txt
```

Upgrade dependencies 
```bash
pip install --upgrade yfinanc
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Jenishh43/Trading_Levels.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Trading_Levels
   ```
3. Run the Python script:
   ```bash
   python trading_levels.py
   ```

## Usage
- Enter the stock ticker symbol (e.g., AAPL, TSLA).
- Input the time period for data fetching (e.g., 1mo, 1d).
- Set the accuracy level for support/resistance detection.
- Click "Fetch Data" to visualize the candlestick chart with support and resistance levels.

## Code Overview
- **fetch_Data**: Fetches stock data, calculates support and resistance levels, and plots the candlestick chart.
- **on_submit**: Handles user inputs from the GUI and calls `fetch_Data`.
- **Tkinter GUI**: Provides an interface for the user to input parameters and visualize stock data.

1.![image](https://github.com/user-attachments/assets/bc79dd2b-e0b3-4f66-92c1-b82e7b14fbde)

2.![image](https://github.com/user-attachments/assets/0a3aef42-2a3a-4324-8919-7af73d2cefcf)


## License
This project is licensed under the MIT License.

## Author
[Jenishh43](https://github.com/Jenishh43)
