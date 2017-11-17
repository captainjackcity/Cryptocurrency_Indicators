from __main__ import *
import get_pricing_data
import pandas
import matplotlib.pyplot as plt
from matplotlib import style

df = get_pricing_data.df

print(df.describe())

#plot data to visually ispect
style.use('ggplot')

ax1 = plt.subplot2grid((6,1),(0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0), rowspan=1, colspan=1, sharex = ax1)

ax1.plot(df.index, df['Low'])
ax1.plot(df.index, df['High'])
ax2.plot(df.index, df['Volume (BTC)'])

plt.show()




