import pandas as pd
import pandas_datareader as web
from datetime import datetime

#functions
def get_ticker(string):
    Tmp = string.split(' ')
    return Tmp[0]

def modify_raw_data(df):
    df=df.drop(index=[0,1])
    df=df.rename(columns={'Attributes':'Dates'})
    df=df.set_index('Dates')
    return(df)

sector_list=['S5ENRS', 'S5MATR', 'S5INDU', 'S5COND', 'S5CONS', 'S5HLTH', 'S5FINL', 'S5INFT', 'S5TELS', 'S5UTIL', 'S5RLST']
index_list = ['energy','material','industrial','consumer_discretionary','consumer_staple','health_care','financial','IT','telecom','utility','real_estate']

#get component code
df=pd.read_excel('/Users/JackRitian/Desktop/sector rotation/sector_summary.xlsx')
sector_codes=df['Component Code'].tolist()

'''
#get component data
missing_stock=[]

for code in ['S5ENRS', 'S5MATR', 'S5INDU', 'S5COND', 'S5CONS', 'S5HLTH', 'S5FINL', 'S5INFT', 'S5TELS', 'S5UTIL', 'S5RLST']:
    df=pd.read_excel('/Users/JackRitian/Desktop/sector rotation/data/sector component/'+str(code)+'.xlsx')
    for ticker in df['Ticker']:
        try:
            stock_ticker=get_ticker(ticker)
            data = web.DataReader([stock_ticker], 'yahoo')
            df = modify_raw_data(data)
            df.to_csv('/Users/JackRitian/Desktop/Yahoo Stock/'+stock_ticker+'.csv')
            print(df)
        except:
            missing_stock.append(stock_ticker)
            print(stock_ticker+' is missing')
    print(code + ' is complete')


#modify data
for sector in sector_list:
    components_df=pd.read_excel('/Users/JackRitian/Desktop/sector rotation/data/sector component/'+str(sector)+'.xlsx')
    for ticker in components_df['Ticker']:
        stock_ticker=get_ticker(ticker)
        df=pd.read_csv('/Users/JackRitian/Desktop/Yahoo Stock/'+stock_ticker+'.csv')
        df=modify_raw_data(df)
        df.to_csv('/Users/JackRitian/Desktop/Yahoo Stock/'+stock_ticker+'.csv')

#drop duplicates
for sector in sector_list:
    components_df=pd.read_excel('/Users/JackRitian/Desktop/sector rotation/data/sector component/'+str(sector)+'.xlsx')
    for ticker in components_df['Ticker']:
        stock_ticker=get_ticker(ticker)
        df=pd.read_csv('/Users/JackRitian/Desktop/Yahoo Stock/'+stock_ticker+'.csv')
        df=df.drop_duplicates(subset='Dates')
        df=df.set_index('Dates')
        df.to_csv('/Users/JackRitian/Desktop/Yahoo Stock/'+stock_ticker+'.csv')
'''

#reconstruct sector index
for sector in sector_list:

    components_df=pd.read_excel('/Users/JackRitian/Desktop/sector rotation/data/sector component/'+str(sector)+'.xlsx')

    for ticker in components_df['Ticker']:
        stock_ticker=get_ticker(ticker)
        df=pd.read_csv('/Users/JackRitian/Desktop/Yahoo Stock/'+stock_ticker+'.csv',parse_dates=['Dates'])
        df=df.set_index('Dates')

        if ticker == components_df['Ticker'][0]:
            new_sector_df=df['Close'].to_frame()
            new_sector_df=new_sector_df.rename(columns={'Close':stock_ticker})
        else:
            new_sector_df=new_sector_df.join(df['Close'],on='Dates',how='outer')
            new_sector_df=new_sector_df.rename(columns={'Close':stock_ticker})

    new_sector_df = new_sector_df.backfill()
    new_sector_index = new_sector_df.mean(axis=1)
    new_sector_index = new_sector_index.to_frame().set_axis([sector],axis='columns')
    if sector == sector_list[0]:
        ew_sector_index = new_sector_index
    else:
        ew_sector_index = ew_sector_index.join(new_sector_index)


ew_sector_index = ew_sector_index.set_axis(index_list,axis='columns')

print(ew_sector_index.isna())
ew_sector_index.to_csv('/Users/JackRitian/Desktop/sector rotation/data/ew_sector_index.csv')
