from __main__ import *
import get_pricing_data
import numpy as np
from stockstats import StockDataFrame as Sdf

df = get_pricing_data.df
###Add Indicators
df.columns.values[4] = "volume"
stock_df = Sdf.retype(df)

#add rsi to data frame
df['rsi'] = stock_df['rsi_14']
#add cr
stock_df = Sdf.retype(df)
df['cr'] = stock_df['cr']
df[df.cr > 800] = 800

#add kdj
stock_df['kdjk']
stock_df['kdjd']
stock_df['kdjj']

#add macd and macdsignal
stock_df = Sdf.retype(df)
df['macd'] = stock_df['macd']
stock_df = Sdf.retype(df)
df['macds'] = stock_df['macds']

#add vr
stock_df = Sdf.retype(df)
df['vr'] = stock_df['vr']

df[df.vr > 800] = 800

#add price change
df['open_2_d'] = stock_df['open_2_d']

df.replace(-np.inf, np.nan)
df = df.dropna()
#print(df.tail())
