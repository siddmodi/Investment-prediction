import pandas as pd
import os
import datetime as dt
import logging

# Prepare dataframe of 20k rows and 37 columns
# Last column with 0 and 1

STAGE = "FETCHING DATA WITH API" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

try:
    path = 'dataset\\nifty 100'
    l = os.listdir(path)

    lst = []
    for i in l:
        df1 = pd.read_csv(path+'\\'+i).T.drop(['0'])
        lst.append(df1)
        
    df = pd.concat(lst, ignore_index=True)
    df[36] = df[36].astype(int)

    df.to_csv('dataset\\df.csv')
    logging.info(f'Dataframe created {df}')

except Exception as e:
    logging.exception(f'Error occured while creating dataframe : {e}')
