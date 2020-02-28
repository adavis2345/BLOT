import os
import requests
import json

#*******************************************************************************************************************#
#API Requirements
#*******************************************************************************************************************#

symbol = input("Please enter a stock symbol: ")
symbol = symbol.upper()

request = requests.get("https://finnhub.io/api/v1/stock/upgrade-downgrade?symbol={}&token={}"
                       .format(symbol, os.environ['api_token_finn']))

symbol_data = request.json()

new = []
counter = 0

for item in symbol_data:
    new.append(symbol_data[counter]["toGrade"])
    counter += 1

print(new)