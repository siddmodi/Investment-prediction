from flask import Flask, render_template, request
from flask_cors import cross_origin
import joblib
import numpy as np
import pandas as pd
import os
import joblib
from sklearn import pipeline
from flask import redirect, url_for
import yfinance as yf
import datetime as dt
os.getcwd()

data_pipeline = joblib.load(open('pipeline.joblib','rb'))

app = Flask(__name__)

@app.route('/')
@cross_origin()
def home():
  return render_template('home.html')


@app.route('/predict', methods=['POST','GET'])
@cross_origin()
def predict():
  l1 = []
  stock = str(request.form['stock'])
  stock = stock.upper()
  stock1 = stock.upper()+'.NS'
  l1.append(stock1)

  for j in l1:
    global_array=np.array([0]*37)
    print(global_array.shape)

    for i in range(1):
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
 ################################################
  if yf.download(l1[0],period='1d').empty:
    df2 = df.T
    df2.drop(0,inplace=True)
    df2.drop([36],axis=1,inplace=True)
  else:
    df = df.T
    df.drop(0,inplace=True)
    df.drop([0,1,2,3,36],axis=1,inplace=True)

    df1 = pd.DataFrame(yf.download(l1[0],period='1d')).drop(['Adj Close','Volume'],axis=1,)
    df1 = df1.reset_index()[['Open','High','Low','Close']]
    df1.rename(columns = {'Open':36, 'High':37,'Low':38,'Close':39 }, inplace = True)

    df = df.reset_index(drop=True)
    df1 = df1.reset_index(drop=True)
    df2 = pd.concat([df,df1],axis=1)

    dick={}

    x=[]
    for i in range(36):
      x.append(str(i))

    y=[]
    for i in range(4,40):
      y.append(i)

    for i,j in zip(y,x):
      dick[i]=j

    df2.rename(columns=dick,inplace=True)
################################

    prediction = data_pipeline.predict(df2)

    if prediction == 0:
      output = "I don't recommend you to buy {} stock".format(stock)
    elif prediction == 1:
      output = "I recommend you to buy {} stock".format(stock)

    return render_template('home.html',symbol=stock,prediction_text=f"{output}")

if __name__ == "__main__":
    app.run(debug=True)
