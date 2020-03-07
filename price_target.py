import os
import requests
import json
import datetime

#*******************************************************************************************************************#
#API Requirements
#*******************************************************************************************************************#

symbol = input("Please enter a stock symbol: ")
symbol = symbol.upper()

requestA = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}"
                           "&apikey={}".format(symbol, os.environ['api_token_av']))

request = requests.get("https://finnhub.io/api/v1/stock/price-target?symbol={}&token={}"
                       .format(symbol, os.environ['api_token_finn']))

symbol_data = request.json()
symbol_price = requestA.json()

#Grabbing today for stock price date checker, if its the weekend it gets previous week day
today = datetime.date.today()
if today.isoweekday() in {6, 7}:
    today -= datetime.timedelta(days=today.isoweekday() % 5)
    today = datetime.datetime.strptime(today, '%Y-%m-%d')

symbol_price = symbol_price["Time Series (Daily)"]["{}".format(today)]["4. close"]
symbol_data = symbol_data["targetMean"]

print("{} currently has a price target of {}, its current price is {}.".format(symbol,symbol_data,symbol_price))

