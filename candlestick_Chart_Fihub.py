import plotly.graph_objects as go
import requests
from datetime import datetime, timedelta
import json

#*******************************************************************************************************************#
#API Requirements
#*******************************************************************************************************************#

#Setting current timestamp in Unix as API only uses that format#

to_date_conversion = datetime.now().timestamp()
to_date = str(to_date_conversion).split('.')[0]
from_date_nowDiff = datetime.now() - timedelta(30)
from_date_conversion = from_date_nowDiff.timestamp()
from_date = str(from_date_conversion).split('.')[0]

#API Request Setup#

symbol = input("Please choose a symbol: ")
symbol = symbol.upper()

api_token = "bp89lofrh5r8okvp0p8g"
resolution = 30

request = requests.get("https://finnhub.io/api/v1/stock/candle?symbol="
                 "{}&resolution={}&from={}&to={}&token={}".format(symbol, resolution, from_date, to_date, api_token))

symbol_data = request.json()

#**************************************************************************************************************#
#Candlestick Graph from Plotly
#**************************************************************************************************************#

dates = []
today = datetime.now()
for n in range(1, 31):
    date = today - timedelta(days=n)
    date_day = date.day
    date_month = date.month
    date_year = date.year
    dates.append({"year": date_year, "month": date_month, "day": date_day})

open_data = symbol_data['o']
high_data = symbol_data['h']
low_data = symbol_data['l']
close_data = symbol_data['c']
dates = [datetime(year=dates[29:30][0].get("year"), month=dates[29:30][0].get("month"), day=dates[29:30][0].get("day")),
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
