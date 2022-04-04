import yfinance as yf
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime as dt
import logging
import os


STAGE = "FETCHING DATA WITH API" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

################# for nifty 50 stocks ##########################

try:
    df = pd.read_csv('dataset\\ind_nifty50list.csv')
    l = list(df['Symbol'])
    l1 = []
    for i in l:
        l1.append(i+'.NS')
    logging.info(f'list of all nifty 50 tickers created : {l1}')

except Exception as e:
    logging.exception(f'Error occured while creating a list of nifty 50 tickers {e}')
  

try:
    # for nifty50 take range of i to 240
    for j in l1:
        global_array=np.array([0]*37)
        print(global_array.shape)

        for i in range(240):
            end=dt.datetime.today()-dt.timedelta(i)
            temp_df=pd.DataFrame()
            x=0
            while(len(temp_df)<10):
                end2=dt.datetime.today()-dt.timedelta(x+i)
                start=end2-dt.timedelta(1)
                data = yf.download(j,start,end2)
                #print(data)
                print(end2)
                #print(temp_df)
                print(start)
                temp_df=temp_df.append(data,ignore_index=True)
                x+=1
            print(data)
            data=pd.DataFrame(temp_df)
            final_row=data.iloc[9,:]
            target=int(final_row['Close']>final_row['Open'])
            data.reset_index(inplace=True)
            print(data)
            data=data[0:9].drop(columns={'index','Volume','Adj Close'},axis=1)
            array=data.values.flatten()
            array=np.append(array,target)
            print(array.shape)
            print(global_array.shape)
            print(array)
            global_array=np.column_stack((global_array,array))
            print(global_array)
        df=pd.DataFrame(global_array)
        df.to_csv(f'{j}.csv',index=False)
        files.download(f'{j}.csv')
        logging.info('Dataset downloaded for nifty 50 stocks')

except Exception as e:
    logging.exception(f'Error occured while fetching data of nifty 50 tickers {e}')


################# for nifty next 50 stocks ##########################

try:
    df = pd.read_csv('datase\ind_nifty50list.csv')
    l = list(df['Symbol'])
    l1 = []
    for i in l:
        l1.append(i+'.NS')
    logging.info(f'list of all nifty next 50 tickers created : {l1}')
except Exception as e:
    logging.exception(f'Error occured while creating a list of nifty 50 tickers {e}')


try:
    # for nifty next 50 take range of i to 180
    for j in l1:
        global_array=np.array([0]*37)
        print(global_array.shape)

        for i in range(180):
            end=dt.datetime.today()-dt.timedelta(i)
            temp_df=pd.DataFrame()
            x=0
            while(len(temp_df)<10):
                end2=dt.datetime.today()-dt.timedelta(x+i)
                start=end2-dt.timedelta(1)
                data = yf.download(j,start,end2)
                #print(data)
                print(end2)
                #print(temp_df)
                print(start)
                temp_df=temp_df.append(data,ignore_index=True)
                x+=1
            print(data)
            data=pd.DataFrame(temp_df)
            final_row=data.iloc[9,:]
            target=int(final_row['Close']>final_row['Open'])
            data.reset_index(inplace=True)
            print(data)
            data=data[0:9].drop(columns={'index','Volume','Adj Close'},axis=1)
            array=data.values.flatten()
            array=np.append(array,target)
            print(array.shape)
            print(global_array.shape)
            print(array)
            global_array=np.column_stack((global_array,array))
            print(global_array)
        df=pd.DataFrame(global_array)
        df.to_csv(f'{j}.csv',index=False)
        files.download(f'{j}.csv')
        logging.info('Dataset downloaded for nifty next 50 stocks')

except Exception as e:
    logging.exception(f'Error occured while fetching data of nifty next 50 tickers {e}')
