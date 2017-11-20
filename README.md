# Cryptocurrency_Indicators
This project will use common financial indicators to predict the value of cryptocurrencies. The pattens of Bitcoin prices and there correlation to financial indicator will be examined, analyzed, and plotted. Then, the machine learning random forest regressor algorithm will be applied to make predictions about prices. Bitcoin used in the example but could be applied to other cryptocurrencies.

## Getting Started
Download python scripts from GitHub repo.

### Prerequisits
Get Quandl API key from Quandl.com
Download Python 3.4 from Python.org

### Installing
The installation process varies depending on your python version and system used. However in most cases the following should work:

```shell
pip install quandl
```
```shell
pip install numpy
```
```shell
pip install pandas
```
```shell
pip install matplotlib
```
```shell
pip install stockstats
```

## Run Some Tests

Pull financial data for Bitcoin from Quandl API.
Pricing data includes open, high, low, close, volume, volume (currency), and weighted price.

```python
import quandl
import numpy as np

#authtoken = <your_authtoken>
quandl.ApiConfig.api_key = "<your authtoken>"
#authtoken = quandl.ApiConfig.api_key = "<your authtoken>"

#start_date = "pick_start_date"
start_date = "2016-11-16"

#market = "Pick_market_of_interest"
market = "BCHARTS/BITSTAMPUSD"

#df = quandl.get("BCHARTS/BITSTAMPUSD", authtoken="<your authtoken>", start_date="2016-11-16", parse_dates=True, index_col=0)
#print(df.head())

df = quandl.get(market, authtoken = quandl.ApiConfig.api_key, start_date= start_date, parse_dates=True, index_col=0)
#print(df.head())
```

Inspect dataframe for missing data and common statistics, Plot data

``python pricing_stats.py``

Add financial indicators using stockstats
``python Stock_indicators.py``

Use sklearn package to apply random forests algorithm and create a model. Model will predict open_2_d based on financial indicators open, volume, rsi, cr, macdh, vr. 
``python RF_model.py``

Use model to predict price of cryptocurrency 2 days in the future.
``python Predictor.py``

## Deployment
Model running with score of around 0.8
Some other indicators should be added to improve model. Public Interest variable would be a great addition.
