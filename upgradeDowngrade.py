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

rating = ''

#Buy +1
strongBuy_total = new.count('Strong Buy')
buy_total = new.count('Buy')
positive_total = new.count('Positive')
outperform_total = new.count('Outperform')
overweight_total = new.count('Overweight')

#Sell -1
strongSell_total = new.count('Strong Sell')
sell_total = new.count('Sell')
reduce_total = new.count('Reduce')
negative_total = new.count('Negative')
neutral_total = new.count('Neutral')

#Neutral + or - depending on Buy:Sell ratio
market_total = new.count('Market Perform')
hold_total = new.count('Hold')
equal_total = new.count('Equal-Weight')

more = strongBuy_total + buy_total + positive_total + outperform_total + overweight_total
less = strongSell_total + sell_total + reduce_total + negative_total + neutral_total
even = (market_total + hold_total + equal_total)/2

if more > less:
    real_total = (more - less + even) / 2

elif less > more:
    real_total = (more - less - even) / 1

else:
    real_total = (more - less) / 1


real_total = real_total/100
real_total = real_total * 100

if real_total > 50:
    rating = 'Buy'
    print("{} is considered a {} with a {}% score".format(symbol, rating, round(real_total)))
elif real_total < 25:
    rating = 'Sell'
    print("{} is considered a {} with a {}% score".format(symbol, rating, round(real_total)))
else:
    rating = 'Hold'
    print("{} is considered a {} with a {}% score".format(symbol, rating, round(real_total)))


