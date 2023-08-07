import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


startDate = datetime(2019,2,1)
endDate = datetime(2022,2,24)
trade_taget = 2


def get_top_bot(int):
    if int >= 12-trade_taget:
        return -1
    elif int <= trade_taget:
        return 1
    else:
        return 0

def cal_rtn(signal_df, rtn_df, startDate, endDate):
    mom_sig = signal_df
    index_list = ['energy','material','industrial','consumer_discretionary','consumer_staple','health_care','financial','IT','telecom','utility','real_estate']
    date_list = mom_sig.index.to_list()

    for index in index_list:
        for date in date_list:
            mom_sig.loc[date, index]=get_top_bot(signal_df[index][date])

    #adjust time period
    mom_sig = mom_sig.truncate(before=startDate,after=endDate)
    monthly_mom_sig = mom_sig.resample('M').last().dropna()
    monthly_index_rtn_next = rtn_df.truncate(before=startDate,after=endDate)
    #calculate return & sharpe ratio
    monthly_mom_rtn = (monthly_mom_sig * monthly_index_rtn_next).dropna().sum(axis=1)
    yearly_mom_rtn_mean = monthly_mom_rtn.mean() * 12
    yearly_mom_rtn_std = monthly_mom_rtn.std() * 12**0.5
    yearly_mom_SR = yearly_mom_rtn_mean / yearly_mom_rtn_std
    print('The Average Annual Return Rate is ', yearly_mom_rtn_mean)
    print('The Sharpe Ratio is '+ str(yearly_mom_SR))

    plt.figure()
    plt.title('MOM Factor Returns on Equally-Weighted Index')
    monthly_mom_rtn.cumsum().plot()
    return

def calculate_ts_raw_mom_sig(index_rtn, int_days,startDate,endDate):

    recent_days = int(np.floor(0.1*int_days))
    MOM_sig_raw = index_rtn.shift(recent_days).rolling(int_days-recent_days).sum().dropna()
    MOM_sig_rank = MOM_sig_raw.rank(axis=1, ascending=False).astype(int)
    return MOM_sig_rank

def calculate_ts_norm_mom_sig(index_rtn, int_days,startDate,endDate):
    recent_days = int(np.floor(0.1*int_days))
    MOM_sig_raw = index_rtn.shift(recent_days).rolling(int_days-recent_days).sum().dropna().truncate(before=startDate,after=endDate)
    MOM_sig_mean = MOM_sig_raw.mean(axis=0).dropna()
    MOM_sig_std = MOM_sig_raw.std(axis=0).dropna()
    MOM_sig_raw = MOM_sig_raw.truncate(before=startDate,after=endDate)
    MOM_sig_norm = MOM_sig_raw.sub(MOM_sig_mean).div(MOM_sig_std).dropna()
    MOM_sig_rank = MOM_sig_norm.rank(axis=1, ascending=False).astype(int)
    return MOM_sig_rank

def calculate_crosec_mom_sig(index_rtn, int_days,startDate,endDate):

    recent_days = int(np.floor(0.1*int_days))

    MOM_sig_raw = index_rtn.shift(recent_days).rolling(int_days-recent_days).sum().dropna().truncate(before=startDate,after=endDate)

    MOM_sig_mean = MOM_sig_raw.mean(axis=1)

    MOM_sig_std = MOM_sig_raw.std(axis=1)

    MOM_sig_norm = MOM_sig_raw.sub(MOM_sig_mean,axis=0).div(MOM_sig_std,axis=0)

    MOM_sig_rank = MOM_sig_norm.rank(axis=1, ascending=False).astype(int)


    return MOM_sig_rank

'''
------------------------------------------------------On Real index--------------------------------------------------------------------------------------------------------------------------------------
'''
#startDate = datetime(2017,1,1)
startDate = datetime(2002,1,1)
endDate = datetime(2022,2,24)

df_index=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/sector_index.csv",parse_dates=['Date']).dropna()
df_index=df_index.set_index('Date')
index_rtn = df_index.pct_change().dropna()

#calculate montly return
monthly_index = df_index.resample('M').last().dropna()
monthly_index_rtn = monthly_index.pct_change().dropna()
monthly_index_rtn_next = monthly_index_rtn.shift(-1).dropna() #shift next day's return to today

'''
for period in ['21','42','63','84','105','126','147','168','189','210','231','252']:
    mom_rank=calculate_crosec_mom_sig(index_rtn, int(period) , startDate, endDate)

    print('For Actual Index:')
    cal_rtn(mom_rank, monthly_index_rtn_next, startDate,endDate)
'''

'''
------------------------------------------------------------On The Equally Weighted Index--------------------------------------------------------------------------------------------------
'''

startDate = datetime(2017,5,1)
endDate = datetime(2022,2,24)

#import data
ew_index=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/ew_sector_index.csv",parse_dates=['Date']).dropna()
ew_index=ew_index.set_index('Date')
ew_index_rtn = ew_index.pct_change().dropna()

#calculate montly return
monthly_ew_index = ew_index.resample('M').last().dropna()
monthly_ew_index_rtn = monthly_ew_index.pct_change().dropna()
monthly_ew_index_rtn_next = monthly_ew_index_rtn.shift(-1).dropna() #shift next day's return to today



for period in ['21','42','63','84','105','126','147','168','189','210','231','252']:
    mom_rank=calculate_crosec_mom_sig(ew_index_rtn, int(period) , startDate, endDate)

    print('For Equally Weighted Index:')
    cal_rtn(mom_rank, monthly_ew_index_rtn_next, startDate,endDate)

plt.show()

'''
---------------------------------------------------ON Tradable ETF-------------------------------------------------------------------------
'''


df_index=pd.read_csv('/Users/JackRitian/Desktop/sector rotation/data/ETF data/sector_etf.csv',parse_dates=['Date']).dropna()
df_index=df_index.set_index('Date')
index_rtn = df_index.pct_change().dropna()
