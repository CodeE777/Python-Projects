import requests 
import json 
from Envrionment import Environment

time_series_weekly = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=.INX&apikey={Environment.apikey}")

Parsed_time_series = json.loads(time_series_weekly.content)

print(Parsed_time_series)




