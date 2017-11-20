from __main__ import *
import Stock_indicators
import numpy as np

df = Stock_indicators.df
X = df[['open','volume','rsi','cr','macdh','vr']].copy()
Y = df[['open_2_d']]
y = np.ravel(Y)
#y = list(y1.values)
#print(X.tail(10))
#print(y.tail(10))

from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression

regr = RandomForestRegressor(n_estimators=10)
regr.fit(X, y)
score = regr.score(X, y, sample_weight=None)
print(regr.feature_importances_)
print(score)
#df['predictions'] = regr.predict(X)
