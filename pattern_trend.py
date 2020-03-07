import os
import requests
import json

# *******************************************************************************************************************#
# API Requirements
# *******************************************************************************************************************#

symbol = input("Please enter a stock symbol: ")
symbol = symbol.upper()

request = requests.get("https://finnhub.io/api/v1/scan/pattern?symbol={}&resolution=60&token={}"
                       .format(symbol, os.environ['api_token_finn']))

symbol_data = request.json()

symbol_data = symbol_data["points"]

items = []

for item in symbol_data:
    items.append(item["patterntype"])

bullish = items.count("bullish")
bearish = items.count("bearish")
trend = ""

if bullish > bearish:
    trend = "Bullish"
elif bearish > bullish:
    trend = "Bearish"
else:
    trend = "Neutral"

print("Bullish: {}, Bearish {}.  {} has a {} trend.".format(bullish, bearish, symbol, trend))

