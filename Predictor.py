from __main__ import *
import RF_model

stock = RF_model.X
xnew = stock[['open','volume','rsi','cr','macdh','vr']].copy()

xx = xnew[-2:-1]

change = RF_model.regr.predict(xx)
print(RF_model.regr.predict(xx))

price_estimate = xx['open'] - change
print(xx['open'])
print('Estimated open price in two days is ', price_estimate[0])
