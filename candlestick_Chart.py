import os
import plotly.graph_objects as go
import requests
from datetime import datetime, timedelta
import json

#*******************************************************************************************************************#
#API Requirements
#*******************************************************************************************************************#

#API Request Setup#

symbol = input("Please enter a stock symbol: ")
symbol = symbol.upper()

request = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}"
                           "&apikey={}".format(symbol, os.environ['api_token_av']))

symbol_data = request.json()

#**************************************************************************************************************#
#Candlestick Graph from Plotly
#**************************************************************************************************************#

r = request.json()

try:
    r = r['Time Series (Daily)']
except Exception as e:
    print("Error has occurred, you may have entered an incorrect stock symbol.  Please try again.")
else:
    low_price = []
    open_price = []
    close_price = []
    high_price = []
    key_dates = []
    dates = []

    for key in sorted(r, reverse=True)[:31]:
        key_dates.append({"date": key})
        date = datetime.strptime(key, '%Y-%m-%d')
        date_day = date.day
        date_month = date.month
        date_year = date.year
        dates.append({"year": date_year, "month": date_month, "day": date_day})

    for close in sorted(r, reverse=True)[:31]:
        cPrice = r[close]["4. close"]
        close_price.append(cPrice)

    for openP in sorted(r, reverse=True)[:31]:
        oPrice = r[openP]["1. open"]
        open_price.append(oPrice)

    for high in sorted(r, reverse=True)[:31]:
        hPrice = r[high]["2. high"]
        high_price.append(hPrice)

    for low in sorted(r, reverse=True)[:31]:
        lPrice = r[low]["3. low"]
        low_price.append(lPrice)

    open_price.reverse()
    close_price.reverse()
    high_price.reverse()
    low_price.reverse()

    open_data = open_price
    high_data = high_price
    low_data = low_price
    close_data = close_price

    dates = [
        datetime(year=dates[30:31][0].get("year"), month=dates[30:31][0].get("month"), day=dates[30:31][0].get("day")),
        datetime(year=dates[29:30][0].get("year"), month=dates[29:30][0].get("month"), day=dates[29:30][0].get("day")),
        datetime(year=dates[28:29][0].get("year"), month=dates[28:29][0].get("month"), day=dates[28:29][0].get("day")),
        datetime(year=dates[27:28][0].get("year"), month=dates[27:28][0].get("month"), day=dates[27:28][0].get("day")),
        datetime(year=dates[26:27][0].get("year"), month=dates[26:27][0].get("month"), day=dates[26:27][0].get("day")),
        datetime(year=dates[25:26][0].get("year"), month=dates[25:26][0].get("month"), day=dates[25:26][0].get("day")),
        datetime(year=dates[24:25][0].get("year"), month=dates[24:25][0].get("month"), day=dates[24:25][0].get("day")),
        datetime(year=dates[23:24][0].get("year"), month=dates[23:24][0].get("month"), day=dates[23:24][0].get("day")),
        datetime(year=dates[22:23][0].get("year"), month=dates[22:23][0].get("month"), day=dates[22:23][0].get("day")),
        datetime(year=dates[21:22][0].get("year"), month=dates[21:22][0].get("month"), day=dates[21:22][0].get("day")),
        datetime(year=dates[20:21][0].get("year"), month=dates[20:21][0].get("month"), day=dates[20:21][0].get("day")),
        datetime(year=dates[19:20][0].get("year"), month=dates[19:20][0].get("month"), day=dates[19:20][0].get("day")),
        datetime(year=dates[18:19][0].get("year"), month=dates[18:19][0].get("month"), day=dates[18:19][0].get("day")),
        datetime(year=dates[17:18][0].get("year"), month=dates[17:18][0].get("month"), day=dates[17:18][0].get("day")),
        datetime(year=dates[16:17][0].get("year"), month=dates[16:17][0].get("month"), day=dates[16:17][0].get("day")),
        datetime(year=dates[15:16][0].get("year"), month=dates[15:16][0].get("month"), day=dates[15:16][0].get("day")),
        datetime(year=dates[14:15][0].get("year"), month=dates[14:15][0].get("month"), day=dates[14:15][0].get("day")),
        datetime(year=dates[13:14][0].get("year"), month=dates[13:14][0].get("month"), day=dates[13:14][0].get("day")),
        datetime(year=dates[12:13][0].get("year"), month=dates[12:13][0].get("month"), day=dates[12:13][0].get("day")),
        datetime(year=dates[11:12][0].get("year"), month=dates[11:12][0].get("month"), day=dates[11:12][0].get("day")),
        datetime(year=dates[10:11][0].get("year"), month=dates[10:11][0].get("month"), day=dates[12:13][0].get("day")),
        datetime(year=dates[9:10][0].get("year"), month=dates[9:10][0].get("month"), day=dates[9:10][0].get("day")),
        datetime(year=dates[8:9][0].get("year"), month=dates[8:9][0].get("month"), day=dates[8:9][0].get("day")),
        datetime(year=dates[7:8][0].get("year"), month=dates[7:8][0].get("month"), day=dates[7:8][0].get("day")),
        datetime(year=dates[6:7][0].get("year"), month=dates[6:7][0].get("month"), day=dates[6:7][0].get("day")),
        datetime(year=dates[5:6][0].get("year"), month=dates[5:6][0].get("month"), day=dates[5:6][0].get("day")),
        datetime(year=dates[4:5][0].get("year"), month=dates[4:5][0].get("month"), day=dates[4:5][0].get("day")),
        datetime(year=dates[3:4][0].get("year"), month=dates[3:4][0].get("month"), day=dates[3:4][0].get("day")),
        datetime(year=dates[2:3][0].get("year"), month=dates[2:3][0].get("month"), day=dates[2:3][0].get("day")),
        datetime(year=dates[1:2][0].get("year"), month=dates[1:2][0].get("month"), day=dates[1:2][0].get("day")),
        datetime(year=dates[0:1][0].get("year"), month=dates[0:1][0].get("month"), day=dates[0:1][0].get("day"))]

    fig = go.Figure(data=[go.Candlestick(x=dates,
                                         open=open_data, high=high_data,
                                         low=low_data, close=close_data)])

    fig.show()





