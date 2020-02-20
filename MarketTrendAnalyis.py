import requests 
import json 
from Envrionment import Environment
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Get daily stock market data from alphavantage
time_series_daily = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=.INX&apikey={Environment.apikey}")

# Parse JSON and drill down into 'Time Series (Daily)' dictionary
parsed_time_series = json.loads(time_series_daily.content)['Time Series (Daily)']

# Cast dictionary keys to list of strings (dates)
date_strings = list(parsed_time_series.keys())

# Cast dictionary values to list of strings (all daily market values)
time_series_vals = list(parsed_time_series.values())

# Transform list of string to list of matplotlib.dates
dates = list(map((lambda date_string: mdates.datestr2num(date_string)), date_strings))

# Transform daily market dictionaries to only include closing vals
mkt_close_values = list(map(lambda vals: float(vals['4. close']), time_series_vals))

# Configure x axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

# Plot
plt.plot(dates, mkt_close_values)
plt.show()