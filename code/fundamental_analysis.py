import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier

startDate = datetime(2012,12,1)
endDate = datetime(2021,12,1)

#clean data functions
sector_dict={
            'S&P 500 Materials Sector GICS Level 1 Index': 'material',
            'S&P 500 Energy Sector GICS Level 1 Index':	'energy',
            'S&P 500 Industrials Sector GICS Level 1 Index':'industrial',
            'S&P 500 Consumer Discretionary Sector GICS Level 1 Index':'consumer_discretionary',
            'S&P 500 Consumer Staples Sector GICS Level 1 Index':'consumer_staple',
            'S&P 500 Health Care Sector GICS Level 1 Index':'health_care',
            'S&P 500 Information Technology Sector GICS Level 1 Index':'IT',
            'S&P 500 Financials Sector GICS Level 1 Index': 'financial',
            'S&P 500 Real Estate Sector GICS Level 1 Index': 'real_estate',
            'S&P 500 Utilities Sector GICS Level 1 Index': 'utility',
            'S&P 500 Communication Services Sector GICS Level 1 Index':'telecom'
            }

sector_list = ['energy','material','industrial','consumer_discretionary','consumer_staple','health_care','financial','IT','telecom','utility','real_estate']

def clean_fdmt_data(df):
    df=df.drop(columns=['Unnamed: 0'])
    df=df.rename(columns={'3 Months Ending':'Dates'})
    df=df.set_index('Dates')
    df=df.rename(columns=sector_dict)
    df=df.truncate(after=endDate)
    return(df)

def factor_neutralize(df):
    df_cal=df.dropna()
    df_mean = df_cal.mean(axis=0)
    df_std = df_cal.std(axis=0)
    df_neutral = (df-df_mean)/df_std
    return(df_neutral)

def get_factor_exposure(sector):
    rename_dict={sector:'PE'}
    PE_exposures=PE_neutral[sector].fillna(value=0).to_frame().rename(columns=rename_dict)

    rename_dict={sector:'PB'}
    PB_exposures=PB_neutral[sector].fillna(value=0).to_frame().rename(columns=rename_dict)

    rename_dict={sector:'EV2Sales'}
    EV2Sales_exposures=EV2Sales_neutral[sector].fillna(value=0).to_frame().rename(columns=rename_dict)

    rename_dict={sector:'EV2EBIT'}
    EV2EBIT_exposures=EV2EBIT_neutral[sector].fillna(value=0).to_frame().rename(columns=rename_dict)

    rename_dict={sector:'EV2EBITDA'}
    EV2EBITDA_exposures=EV2EBITDA_neutral[sector].fillna(value=0).to_frame().rename(columns=rename_dict)

    rename_dict={sector:'DIV_Y'}
    DIV_Y_exposures=DIV_Y_neutral[sector].fillna(value=0).to_frame().rename(columns=rename_dict)

    rename_dict={sector:'GM'}
    GM_exposures=GM_neutral[sector].fillna(value=0).to_frame().rename(columns=rename_dict)

    rename_dict={sector:'OM'}
    OM_exposures=OM_neutral[sector].fillna(value=0).to_frame().rename(columns=rename_dict)

    rename_dict={sector:'PM'}
    PM_exposures=PM_neutral[sector].fillna(value=0).to_frame().rename(columns=rename_dict)

    rename_dict={sector:'ROA'}
    ROA_exposures=ROA_neutral[sector].fillna(value=0).to_frame().rename(columns=rename_dict)

    rename_dict={sector:'ROE'}
    ROE_exposures=ROE_neutral[sector].fillna(value=0).to_frame().rename(columns=rename_dict)

    factor_exposure=PE_exposures.join(PB_exposures).join(EV2Sales_exposures).join(EV2EBIT_exposures).join(EV2EBITDA_exposures).join(DIV_Y_exposures).join(GM_exposures).join(OM_exposures).join(PM_exposures).join(ROA_exposures).join(ROE_exposures)

    return(factor_exposure)



#import&clean Data
#PE ratio
df=pd.read_excel('/Users/JackRitian/Desktop/sector rotation/data/Fundamentals/PE Ratio.xlsx',parse_dates=['3 Months Ending'])
PE_df=clean_fdmt_data(df)
PE_neutral=factor_neutralize(PE_df)


#PB ratio
df=pd.read_excel('/Users/JackRitian/Desktop/sector rotation/data/Fundamentals/PB Ratio.xlsx',parse_dates=['3 Months Ending'])
PB_df=clean_fdmt_data(df)
PB_neutral=factor_neutralize(PB_df)

#EV2Sales
df=pd.read_excel('/Users/JackRitian/Desktop/sector rotation/data/Fundamentals/EV2Sales.xlsx',parse_dates=['3 Months Ending'])
EV2Sales_df=clean_fdmt_data(df)
EV2Sales_neutral=factor_neutralize(EV2Sales_df)

#EV2EBIT
df=pd.read_excel('/Users/JackRitian/Desktop/sector rotation/data/Fundamentals/EV2EBIT.xlsx',parse_dates=['3 Months Ending'])
EV2EBIT_df=clean_fdmt_data(df)
EV2EBIT_neutral=factor_neutralize(EV2EBIT_df)

#EV2EBITDA
df=pd.read_excel('/Users/JackRitian/Desktop/sector rotation/data/Fundamentals/EV2EBITDA.xlsx',parse_dates=['3 Months Ending'])
EV2EBITDA_df=clean_fdmt_data(df)
EV2EBITDA_neutral=factor_neutralize(EV2EBITDA_df)

#Dividend Yield
df=pd.read_excel('/Users/JackRitian/Desktop/sector rotation/data/Fundamentals/Dividend Yield.xlsx',parse_dates=['3 Months Ending'])
DIV_Y_df=clean_fdmt_data(df)
DIV_Y_neutral=factor_neutralize(DIV_Y_df)

#Gross Margin
df=pd.read_excel('/Users/JackRitian/Desktop/sector rotation/data/Fundamentals/Gross Margin.xlsx',parse_dates=['3 Months Ending'])
GM_df=clean_fdmt_data(df)
GM_neutral=factor_neutralize(GM_df)

#Operating Margin
df=pd.read_excel('/Users/JackRitian/Desktop/sector rotation/data/Fundamentals/operatingmargin.xlsx',parse_dates=['3 Months Ending'])
OM_df=clean_fdmt_data(df)
OM_neutral=factor_neutralize(OM_df)

#profit Margin
df=pd.read_excel('/Users/JackRitian/Desktop/sector rotation/data/Fundamentals/profit margin.xlsx',parse_dates=['3 Months Ending'])
PM_df=clean_fdmt_data(df)
PM_neutral=factor_neutralize(PM_df)

#return on asset
df=pd.read_excel('/Users/JackRitian/Desktop/sector rotation/data/Fundamentals/return on asset.xlsx',parse_dates=['3 Months Ending'])
ROA_df=clean_fdmt_data(df)
ROA_neutral=factor_neutralize(ROA_df)

#return on equity
df=pd.read_excel('/Users/JackRitian/Desktop/sector rotation/data/Fundamentals/return on equity.xlsx',parse_dates=['3 Months Ending'])
ROE_df=clean_fdmt_data(df)
ROE_neutral=factor_neutralize(ROE_df)

'''
---------------------------------------------------- Return to Factor Exposure------------------------------------------------------------------------------------
'''

sector_index=pd.read_csv('/Users/JackRitian/Desktop/sector rotation/data/index data/sector_index.csv',parse_dates=['Date'])
sector_index=sector_index.set_index('Date').truncate(before=startDate,after=endDate)
monthly_index_rtn=sector_index.resample("Q").last().pct_change().shift(-1).dropna()


def exposure_to_return(factor):
    exposures=[]
    returns=[]
    for sector in sector_list:
        factor_exposure=get_factor_exposure(sector)
        factor_exposure=factor_exposure.truncate(after=endDate)

        for exposure in factor_exposure[factor]:
            exposures.append(exposure)
        for rtn in monthly_index_rtn[sector]:
            returns.append(rtn)


    exposure_to_return={'Neutralized Exposure':exposures,'Return':returns}
    df=pd.DataFrame(exposure_to_return)


    df.plot.scatter(x='Neutralized Exposure',y='Return')
    plt.title(factor+' to Return')
    plt.show()
    return(df)


factor_list=['PE','PB','EV2Sales','EV2EBIT','EV2EBITDA','DIV_Y','GM','OM','PM','ROA','ROE']

for factor in factor_list:
    if factor == factor_list[0]:

        df = exposure_to_return(factor).rename(columns={'Neutralized Exposure':factor})
    else:
        new_df = exposure_to_return(factor).rename(columns={'Neutralized Exposure':factor}).drop(columns=['Return'])
        df=df.join(new_df)

for i in range(0,len(df['Return'])):
    if df['Return'][i] >= 0:
        df.loc[i,'Return']=1
    else:
        df.loc[i,'Return']=-1

def split_sets(df,x_list,y_name):

    df = df.sample(frac=1).reset_index(drop=True)
    first_cut=int(np.floor(0.6*len(df[y_name])))
    second_cut=int(np.floor(0.8*len(df[y_name])))

    Y_train = df[y_name][0:first_cut]
    X_train = df[x_list][0:first_cut]
    X_train = X_train.to_numpy()
    Y_train = Y_train.to_numpy()

    Y_valid = df[y_name][first_cut:second_cut]
    Y_valid = Y_valid.reset_index(drop=True)
    X_valid = df[x_list][first_cut:second_cut]
    X_valid = X_valid.reset_index(drop=True)
    X_valid = X_valid.to_numpy()
    Y_valid = Y_valid.to_numpy()

    Y_test = df[y_name][second_cut:]
    Y_test = Y_test.reset_index(drop=True)
    X_test = df[x_list][second_cut:]
    X_test = X_test.reset_index(drop=True)
    X_test = X_test.to_numpy()
    Y_test = Y_test.to_numpy()


    return X_train, Y_train, X_valid, Y_valid, X_test, Y_test

X_train, Y_train, X_valid, Y_valid, X_test, Y_test = split_sets(df,factor_list,'Return')


clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(11, 2), random_state=1)
clf.fit(X_train, Y_train)


y_pred=clf.predict(X_valid)
print(y_pred)

'''
----------------------------------------------------profit ability------------------------------------------------------------------------------------


#ROE2lastyear
ROE2lastyear=ROE_df.backfill().pct_change(periods=4).shift(1).dropna()
ROE2lastyear_sig=ROE2lastyear
dates=ROE2lastyear.index.to_list()

for sector in sector_list:
    try:
        for date in dates:

            if ROE2lastyear[sector][date] > 0:
                ROE2lastyear_sig.loc[date,sector] = 1
            elif ROE2lastyear[sector][date] == 0 :
                ROE2lastyear_sig.loc[date,sector] = 0
            else:
                ROE2lastyear_sig.loc[date,sector] = -1
    except:
        print(sector+' fails calculation')

print(ROE2lastyear_sig)

#ROA2lastyear
ROA2lastyear=ROA_df.backfill().pct_change(periods=4).shift(1).dropna()
ROA2lastyear_sig=ROA2lastyear
dates=ROA2lastyear.index.to_list()

for sector in sector_list:
    try:
        for date in dates:

            if ROA2lastyear[sector][date] > 0:
                ROA2lastyear_sig.loc[date,sector] = 1
            elif ROA2lastyear[sector][date] == 0 :
                ROA2lastyear_sig.loc[date,sector] = 0
            else:
                ROA2lastyear_sig.loc[date,sector] = -1
    except:
        print(sector+' fails calculation')

print(ROA2lastyear_sig)


growth ability
'''
