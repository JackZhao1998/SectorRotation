import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web
from datetime import datetime

index_list=['energy','material','industrial','consumer_discretionary','consumer_staple','health_care','financial','IT','telecom','utility','real_estate']

startDate = datetime(2001, 1, 1)
endDate = datetime(2022,2,24)

'''
df = web.DataReader(['^SP500-55'], 'yahoo', startDate, endDate)
df.to_csv('/Users/JackRitian/Desktop/sector rotation/data/index data/utility_index.csv')

df = web.DataReader(['^SP500-60'], 'yahoo', startDate, endDate)
df.to_csv('/Users/JackRitian/Desktop/sector rotation/data/index data/real_estate_index.csv')

datas=['consumer_discretionary','consumer_staple','health_care']
symbols=['^SP500-25','^SP500-30','^SP500-35']

df = web.DataReader(['^SP500-25'], 'yahoo', startDate, endDate)
df.to_csv('/Users/JackRitian/Desktop/sector rotation/data/index data/consumer_discretionary_index.csv')

df = web.DataReader(['^SP500-30'], 'yahoo', startDate, endDate)
df.to_csv('/Users/JackRitian/Desktop/sector rotation/data/index data/consumer_staple_index.csv')

df = web.DataReader(['^SP500-35'], 'yahoo', startDate, endDate)
df.to_csv('/Users/JackRitian/Desktop/sector rotation/data/index data/health_care_index.csv')
'''


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




df_index=pd.concat([df_energy['Close'],df_material['Close'],df_industrial['Close'],df_consumer_discretionary['Close'],df_consumer_staple['Close'],df_health_care['Close'],df_financial['Close'],df_IT['Close'],df_telecom['Close'],df_utility['Close'],df_real_estate['Close']],axis=1)
df_index=df_index.dropna()
df_index.columns=['energy','material','industrial','consumer_discretionary','consumer_staple','health_care','financial','IT','telecom','utility','real_estate']
print(df_index)
df_index.to_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/sector_index.csv")
