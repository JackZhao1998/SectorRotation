import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

startDate = datetime(2001, 1, 1)
endDate = datetime(2022,2,24)

df_index=pd.read_csv("/Users/JackRitian/Desktop/sector rotation/data/index data/sector_index.csv",parse_dates=['Date']).dropna()
monthly_index=df_index.resample('M',on='Date').last()
monthly_index=monthly_index.drop(columns=['Date'])


'''
covid pandemic
'''

covid_period_data = monthly_index.truncate(before='2020-02-01',after='2022-01-31')
covid_period_data_uniform = covid_period_data.divide(covid_period_data.iloc[0],axis=1)

index_list=[]
for index in covid_period_data_uniform.columns:
    index_list.append(index)

plt.figure(figsize=(10,5))
plt.title("Covid Pandemic")
plt.xlabel("Time by Month")
plt.ylabel("Index")
plt.plot(covid_period_data_uniform)
plt.legend(index_list,loc=2,fontsize='x-small')
plt.show()
