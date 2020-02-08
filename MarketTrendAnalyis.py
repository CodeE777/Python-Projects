import requests 
import json 
from Envrionment import Environment

time_series_weekly = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=.INX&apikey={Environment.apikey}")

parsed_time_series = json.loads(time_series_weekly.content)['Time Series (Daily)']

for date in parsed_time_series:
    print(date)
    print(parsed_time_series[date]['4. close'])

# print(test)

# r1 = { 'fname' : 'Kent', 'lname' : 'Johnson' }
# r2 = { 'fname' : 'Negroup', 'lname' : None }
# data = [ r1, r2 ]

# # Suppose I want to find everyone whose first name is 'Kent'. This is easy to do with a list comprehension:

# test = [ r for r in data if r['fname'] == 'Kent' ]

# print(test)
