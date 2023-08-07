import pandas as pd
import matplotlib.pyplot as plt

df_index=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/sector_index.csv",index_col='Date')


#calculate index returns
df_rtn=df_index.pct_change(fill_method='ffill')
df_rtn_prev=df_rtn.shift(periods=1, freq=None, axis=0, fill_value='NaN')
df_5d_rolling=df_rtn_prev.rolling(5, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None).sum()
df_5d_rolling.dropna(inplace=True)

#mr signal
mr_sig_raw = - df_5d_rolling
mr_sig_mean=mr_sig_raw.mean(axis=1)
mr_sig_std=mr_sig_raw.std(axis=1)
mr_sig_norm=mr_sig_raw.sub(mr_sig_mean,axis='rows', level=None, fill_value=None).div(mr_sig_std, axis='rows', level=None, fill_value=None)

#test mr signal
mr_rtn = (mr_sig_norm/(11-1) * df_rtn).truncate(before='2002-10-10').sum(axis=1)
mr_rtn_mean = mr_rtn.mean() * 252
mr_rtn_std = mr_rtn.std() * 252**0.5
mr_SR = mr_rtn_mean / mr_rtn_std
print('The Mean_Reverse sharpe ratio is ' +str(mr_SR))

print(mr_rtn)
#mom signal
mom_sig_raw = df_rtn.shift(22).rolling(231).sum().dropna()
mom_sig_mean=mom_sig_raw.mean(axis=1)
mom_sig_std=mom_sig_raw.std(axis=1)
mom_sig_norm=mom_sig_raw.sub(mom_sig_mean,axis='rows', level=None, fill_value=None).div(mom_sig_std, axis='rows', level=None, fill_value=None)

#test momentum signal
mom_rtn = (mom_sig_norm/(11-1) * df_rtn).dropna().sum(axis=1)
mom_rtn_mean = mom_rtn.mean() * 252
mom_rtn_std = mom_rtn.std() * 252**0.5
mom_SR = mom_rtn_mean / mom_rtn_std
print('The momentum sharp ratio is '+ str(mom_SR))

#combined strategy
both_rtn = 0.5*mom_rtn + 0.5*mr_rtn
both_rtn_mean = both_rtn.mean() * 252
both_rtn_std = both_rtn.std() * 252**0.5
both_SR = both_rtn_mean / mr_rtn_std
print('The combined strategy sharpe ratio is '+ str(both_SR))



plt.figure()
plt.title('Factor Returns')
mom_rtn.cumsum().plot()
mr_rtn.cumsum().plot()
both_rtn.cumsum().plot()

plt.figure()
plt.title('Factor Returns with 15% Volatility')
(mom_rtn.cumsum()/mom_rtn_std*0.15).plot()
(mr_rtn.cumsum()/mr_rtn_std*0.15).plot()
(both_rtn.cumsum()/both_rtn_std*0.15).plot()

plt.show()
