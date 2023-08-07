from mom_factor import *

startDate = datetime(2002,2,1)
endDate = datetime(2022,2,24)
trade_taget = 2

'''
------------------------------------------------------On Real index--------------------------------------------------------------------------------------------------------------------------------------
'''
startDate = datetime(2017,1,1)
endDate = datetime(2022,2,24)

df_index=pd.read_csv("data/index data/sector_index.csv",parse_dates=['Date']).dropna()
df_index=df_index.set_index('Date')
index_rtn = df_index.pct_change().dropna()
index_rtn_next = index_rtn.shift(-1)

def calculate_reversion_sig(index_rtn, int_days,startDate,endDate):
    rev_sig_raw = -index_rtn.rolling(int_days).sum().dropna()
    rev_sig_rank = rev_sig_raw.rank(axis=1, ascending=False).astype(int)
    return(rev_sig_rank)

for period in ['5','10','15','20','25','30','35','40','45','50','55','60']:
    rev_rank=calculate_reversion_sig(index_rtn, int(period) , startDate, endDate)

    print('For Actual Index:')
    cal_rtn(rev_rank, index_rtn_next, startDate,endDate)
plt.show()
