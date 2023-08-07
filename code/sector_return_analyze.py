import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

startDate = datetime(2001, 1, 1)
endDate = datetime(2022,2,24)


#process data
df_etf=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/ETF data/sector_etf.csv",parse_dates=['Date']).dropna()
df_index=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/sector_index.csv",parse_dates=['Date']).dropna()


#convert to monthly data
monthly_index_rtn=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/monthly_index_return.csv",index_col='Date')
'''
monthly_index=df_index.resample('M',on='Date').last()
monthly_index=monthly_index.drop(columns=['Date'])
monthly_etf=df_etf.resample('M',on='Date').last()
monthly_etf=monthly_etf.drop(columns=['Date'])
monthly_etf_rtn=monthly_etf.pct_change().dropna()
monthly_index_rtn=monthly_index.pct_change().dropna()
'''

#convert to quarterly data
quarterly_index=df_index.resample('Q',on='Date').last()
quarterly_index=quarterly_index.drop(columns=['Date'])
quarterly_index_rtn=quarterly_index.pct_change().dropna()

#convert to yearly data
yearly_index=df_index.resample('Y',on='Date').last()
yearly_index=yearly_index.drop(columns=['Date'])
yearly_index_rtn=yearly_index.pct_change().dropna()



alpha = 0.25

#monthly
index_monthly_rtn_rank = monthly_index_rtn.apply(pd.qcut,axis=1, args=([0,alpha,1-alpha,1.],),labels=[-1/3,0,1/3]).astype('float64')
sector_monthly_difference = index_monthly_rtn_rank*monthly_index_rtn
sector_monthly_difference = sector_monthly_difference.sum(axis=1)
plt.figure()
plt.title('Monthly Return Difference')
sector_monthly_difference.plot()


#quarterly
index_quarterly_rtn_rank = quarterly_index_rtn.apply(pd.qcut,axis=1, args=([0,alpha,1-alpha,1.],),labels=[-1/3,0,1/3]).astype('float64')
sector_quarterly_difference = index_quarterly_rtn_rank*quarterly_index_rtn
sector_quarterly_difference = sector_quarterly_difference.sum(axis=1)
plt.figure()
plt.title('Quarterly Return Difference')
sector_quarterly_difference.plot()


#yearly
index_yearly_rtn_rank = yearly_index_rtn.apply(pd.qcut,axis=1, args=([0,alpha,1-alpha,1.],),labels=[-1/3,0,1/3]).astype('float64')
sector_yearly_difference = index_yearly_rtn_rank*yearly_index_rtn
sector_yearly_difference = sector_yearly_difference.sum(axis=1)
plt.figure()
plt.title('Yearly Return Difference')
sector_yearly_difference.plot()
plt.show()

sector_monthly_difference.to_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/sector_monthly_difference.csv")
sector_quarterly_difference.to_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/sector_quarterly_difference.csv")
sector_yearly_difference.to_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/sector_yearly_difference.csv")
