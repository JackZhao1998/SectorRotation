import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

startDate = datetime(2001, 1, 1)
endDate = datetime(2022,2,24)

#process data
df_etf=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/ETF data/sector_etf.csv",parse_dates=['Date']).dropna()
df_index=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/sector_index.csv",parse_dates=['Date']).dropna()

#convert to monthly data
monthly_index=df_index.resample('M',on='Date').last()
monthly_index=monthly_index.drop(columns=['Date'])
monthly_etf=df_etf.resample('M',on='Date').last()
monthly_etf=monthly_etf.drop(columns=['Date'])
monthly_etf_rtn=monthly_etf.pct_change().dropna()
monthly_index_rtn=monthly_index.pct_change().dropna()

df_index=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/sector_index.csv",index_col='Date')
df_etf=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/ETF data/sector_etf.csv",index_col='Date')

'''
#calculate mr signal
df_index_rtn=df_index.pct_change().dropna()
df_etf_rtn=df_etf.pct_change().dropna()
df_index_rtn_prev=df_index_rtn.shift(periods=1, freq=None, axis=0, fill_value='NaN')
df_index_rolling=df_index_rtn_prev.rolling(5, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None).sum()
df_index_rolling.dropna(inplace=True)
mr_sig_raw = - df_index_rolling

#test mr signal
#.truncate(before='2018-06-30',after='2022-01-31')
mr_rtn = (mr_sig_raw * df_etf_rtn).dropna().sum(axis=1)
mr_rtn_mean = mr_rtn.mean() * 252
mr_rtn_std = mr_rtn.std() * 252**0.5
mr_SR = mr_rtn_mean / mr_rtn_std
print('The Mean_Reverse sharpe ratio on etf is ' +str(mr_SR))

plt.figure()
plt.title('MR ETF Factor Returns')
mr_rtn.cumsum().plot()

mr_rtn = (mr_sig_raw * df_index_rtn).dropna().sum(axis=1)
mr_rtn_mean = mr_rtn.mean() * 252
mr_rtn_std = mr_rtn.std() * 252**0.5
mr_SR = mr_rtn_mean / mr_rtn_std
print('The Mean_Reverse sharpe ratio on index is ' +str(mr_SR))
'''

#momentum
mom_sig_raw = monthly_index_rtn.shift(1).rolling(6).sum().dropna()
mom_sig_mean = mom_sig_raw.mean(axis=1)
mom_sig_std = mom_sig_raw.std(axis=1)
mom_sig_norm = mom_sig_raw.sub(mom_sig_mean,axis='rows', level=None, fill_value=None).div(mom_sig_std, axis='rows', level=None, fill_value=None)

alpha=0.25
mom_sig_rank = mom_sig_raw.apply(pd.qcut,axis=1, args=([0,alpha,1-alpha,1.],),labels=[-1,0,1]).astype('float64')

before_date = '2017-09-01'
after_date = '2022-2-01'
mom_sig_rank = mom_sig_rank.truncate(before=before_date,after=after_date)
monthly_etf_rtn = monthly_etf_rtn.truncate(before=before_date,after=after_date)
monthly_index_rtn = monthly_index_rtn.truncate(before=before_date,after=after_date)

#test momentum signal
mom_index_rtn = (mom_sig_rank * monthly_index_rtn).dropna().sum(axis=1)
mom_index_rtn_mean = mom_index_rtn.mean() * 12
mom_index_rtn_std = mom_index_rtn.std() * 12**0.5
mom_index_SR = mom_index_rtn_mean / mom_index_rtn_std
print('The Momentum Sharp Ratio on index is '+ str(mom_index_SR))

#test momentum signal
mom_etf_rtn = (mom_sig_rank * monthly_etf_rtn).dropna().sum(axis=1)
mom_etf_rtn_mean = mom_etf_rtn.mean() * 12
mom_etf_rtn_std = mom_etf_rtn.std() * 12**0.5
mom_etf_SR = mom_etf_rtn_mean / mom_etf_rtn_std
print('The Momentum Sharp Ratio on etf is '+ str(mom_etf_SR))

plt.figure()
plt.title('MOM ETF Factor Returns')
mom_etf_rtn.cumsum().plot()

plt.figure()
plt.title('MOM INDEX Factor Returns')
mom_index_rtn.cumsum().plot()
plt.show()
