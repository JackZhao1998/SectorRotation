import pandas as pd
import pandas_datareader as web
from datetime import datetime

startDate = datetime(1995, 1, 1)
endDate = datetime(2022,2,24)

index_list=['energy','material','industrial','consumer_discretionary','consumer_staple','health_care','financial','IT','telecom','utility','real_estate']

#import index data
df_energy=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/energy_index.csv",index_col="Date")
df_material=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/material_index.csv",index_col="Date")
df_industrial=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/industrial_index.csv",index_col="Date")
df_consumer_discretionary=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/consumer_discretionary_index.csv",index_col="Date")
df_consumer_staple=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/consumer_staple_index.csv",index_col="Date")
df_health_care=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/health_care_index.csv",index_col="Date")
df_financial=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/financial_index.csv",index_col="Date")
df_IT=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/IT_index.csv",index_col="Date")
df_telecom=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/telecom_index.csv",index_col="Date")
df_real_estate=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/real_estate_index.csv",index_col="Date")
df_utility=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/utility_index.csv",index_col="Date")

#import ETF data
df_xle=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/ETF data/XLE.csv",index_col="Date")
df_xlb=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/ETF data/XLB.csv",index_col="Date")
df_xli=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/ETF data/XLI.csv",index_col="Date")
df_xly=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/ETF data/XLY.csv",index_col="Date")
df_xlp=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/ETF data/XLP.csv",index_col="Date")
df_xlv=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/ETF data/XLV.csv",index_col="Date")
df_xlf=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/ETF data/XLF.csv",index_col="Date")
df_xlk=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/ETF data/XLK.csv",index_col="Date")
df_xlc=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/ETF data/XLC.csv",index_col="Date")
df_xlu=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/ETF data/XLU.csv",index_col="Date")
df_xlre=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/ETF data/XLRE.csv",index_col="Date")

'''
df=pd.concat([df_xle['Close'],df_xlb['Close'],df_xli['Close'],df_xly['Close'],df_xlp['Close'],df_xlv['Close'],df_xlf['Close'],df_xlk['Close'],df_xlc['Close'],df_xlu['Close'],df_xlre['Close']],axis=1).dropna()
df.columns=index_list
df.to_csv("/Users/JackRitian/Desktop/sector rotation/data/sector_etf.csv")
print(df)
'''
df_index_rtn=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/sector_index.csv",index_col='Date').pct_change().dropna()
index_cov=df_index_rtn.cov()
index_cov.to_csv("/Users/JackRitian/Desktop/sector rotation/data/sector_rtn_cov.csv")


#Calculate Correlation
data=pd.concat([df_energy['Close'],df_xle['Close']],axis=1).dropna()
data_pct_chg=data.pct_change().dropna()
print("The correlation for energy sector and its ETF is")
print(data_pct_chg.corr())

data=pd.concat([df_material['Close'],df_xlb['Close']],axis=1).dropna()
data_pct_chg=data.pct_change().dropna()
print("The correlation for material sector and its ETF is")
print(data_pct_chg.corr())

data=pd.concat([df_industrial['Close'],df_xli['Close']],axis=1).dropna()
data_pct_chg=data.pct_change().dropna()
print("The correlation for industrial sector and its ETF is")
print(data_pct_chg.corr())

data=pd.concat([df_consumer_discretionary['Close'],df_xly['Close']],axis=1).dropna()
data_pct_chg=data.pct_change().dropna()
print("The correlation for consumer_discretionary sector and its ETF is")
print(data_pct_chg.corr())

data=pd.concat([df_consumer_staple['Close'],df_xlp['Close']],axis=1).dropna()
data_pct_chg=data.pct_change().dropna()
print("The correlation for consumer_staple sector and its ETF is")
print(data_pct_chg.corr())

data=pd.concat([df_health_care['Close'],df_xlv['Close']],axis=1).dropna()
data_pct_chg=data.pct_change().dropna()
print("The correlation for health_care sector and its ETF is")
print(data_pct_chg.corr())

data=pd.concat([df_financial['Close'],df_xlf['Close']],axis=1).dropna()
data_pct_chg=data.pct_change().dropna()
print("The correlation for financial sector and its ETF is")
print(data_pct_chg.corr())

data=pd.concat([df_IT['Close'],df_xlk['Close']],axis=1).dropna()
data_pct_chg=data.pct_change().dropna()
print("The correlation for IT sector and its ETF is")
print(data_pct_chg.corr())

data=pd.concat([df_telecom['Close'],df_xlc['Close']],axis=1).dropna()
data_pct_chg=data.pct_change().dropna()
print("The correlation for telecom sector and its ETF is")
print(data_pct_chg.corr())

data=pd.concat([df_utility['Close'],df_xlu['Close']],axis=1).dropna()
data_pct_chg=data.pct_change().dropna()
print("The correlation for utility sector and its ETF is")
print(data_pct_chg.corr())

data=pd.concat([df_real_estate['Close'],df_xlre['Close']],axis=1).dropna()
data_pct_chg=data.pct_change().dropna()
print("The correlation for real_estate sector and its ETF is")
print(data_pct_chg.corr())

df=pd.read_excel("/Users/JackRitian/Desktop/sector rotation/data/sector_summary.xlsx")
print(pd.concat([df['Sector'],df['Correlation']],axis=1))
