import quandl
import numpy as np

#authtoken = <your_authtoken>
quandl.ApiConfig.api_key = "your_authtoken"


#start_date = "pick_start_date"
start_date = "2016-11-16"

#market = "Pick_market_of_interest"
market = "BCHARTS/BITSTAMPUSD"

#df = quandl.get("BCHARTS/BITSTAMPUSD", authtoken="your_authtoken", start_date="2016-11-16", parse_dates=True, index_col=0)
#print(df.head())

df = quandl.get(market, authtoken = quandl.ApiConfig.api_key, start_date= start_date, parse_dates=True, index_col=0)
#print(df.head())
