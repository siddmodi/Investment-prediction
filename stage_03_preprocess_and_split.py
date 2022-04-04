import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns',5000)
import logging
import os
from sklearn.model_selection import train_test_split

STAGE = "PREPROCESS_&_SPLIT" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

df = pd.read_csv('dataset\\df.csv',index_col=[0])

# missing values drop
try:
    df = df.dropna()
    logging.info('Missing values treated')
except Exception as e:
    logging.exception(f'Error occured while treating missing values {e}')


# drop duplicates
try:
    df.drop_duplicates(keep = 'first', inplace = True)
    logging.info('Duplicates dropped')
except Exception as e:
    logging.exception(f'Error occured while droping duplicates {e}')


# Train-Test Split
try:
    x = df.drop(['36'],axis=1)
    y = df['36']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)
    logging.info('Train_test Split done')
except Exception as e:
    logging.exception(f'Error occured while Train-Test split {e}')











