from pandas import read_csv
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc



style.use('ggplot')
start = dt.datetime(2015,1,1)
end = dt.datetime(2019,1,25)

#df_CSI300 = web.DataReader('CHAD', 'yahoo', start, end) # Direxion Dly CSI 300 Chn A Shr Br 1X ETF (CHAD)
#df_NIFTY50 = web.DataReader('^NSEI', 'yahoo', start, end) # NIFTY 50 (^NSEI)
#df_HSI = web.DataReader('^HSI', 'yahoo', start, end) # HANG SENG INDEX (^HSI)
#df_N225 = web.DataReader('^N225', 'yahoo', start, end) # Nikkei 225 (^N225)
#df_GSPC = web.DataReader('^GSPC', 'yahoo', start, end) # S&P 500 (^GSPC)
#df_DJI = web.DataReader('^DJI', 'yahoo', start, end) # Dow Jones Industrial Average (^DJI)
#df_DJI.to_csv('DJI.csv')

df_DJI = read_csv('DJI.csv', parse_dates=True, index_col=0)

df_DJI['MACD100'] = df_DJI['Adj Close'].rolling(window=100).mean()


plt.figure(figsize = (10, 8))

ax1 = plt.subplot2grid(shape=(8,1), loc=(0,0), rowspan=6, colspan=1)
ax2 = plt.subplot2grid(shape=(8,1), loc=(7,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

# ax1.plot(df_DJI['Adj Close'])
# ax1.plot(df_DJI['MACD'])
# ax1.legend()
# ax2.bar(df_DJI.index, df_DJI['Volume'])

# plt.show()

# RESAMPLING

df_DJI_ohlc = df_DJI['Adj Close'].resample('10D').ohlc()
df_DJI_volume = df_DJI['Volume'].resample('10D').sum()

df_DJI_ohlc.reset_index(inplace=True)

df_DJI_ohlc['Date'] = df_DJI_ohlc['Date'].map(mdates.date2num)

candlestick_ohlc(ax1, df_DJI_ohlc.values, width=5, colorup='g')
ax1.plot(df_DJI['MACD100'])
ax1.legend()
ax2.fill_between(df_DJI_volume.index.map(mdates.date2num), df_DJI_volume.values, 0)

plt.show()

