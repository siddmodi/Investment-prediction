# Investment-prediction

Flask app of investment prediction which tell us whether their is good time for buying any stock or not based on stock previous performance on the basis of 
daily candles high,low,close,open. and we can directly see the chart of that stock from that app for further analysis. we Used yfinance API to extract data
of top 100 nifty stocks and store in database with proper columns in pandas dataframe.

When we Run the prediction it'll hit the API and extract recent real time few days High,Low,Close,Open of that stock and predict whether it's good time to buy or not
based on the trained pipeline that we created with RandomForest classification model. We used StratifiedKFold cross validation for better accuracy and generalize model
We divide this project in 7 stages to smoothen the flow and easy for understanding

**stage_01_fetching_data_with_api** : We fatch data (high,low,close,open) of top 100 nifty stocks daily candles of recent few days with yfinanace API and store 
					in databse with proper naming convention. If there is any holiday or market is off then it'll skip that day automatically
					
**stage_02_dataframe_creation** : This stage create a full flegded dataframe with proper naming convention 

**stage_03_preprocess_and_split** : This'll do all the preprocessing steps and clean the dataframe like drop duplicates, train-test split etc

**stage_04_ct_and_model_selection** : Column transformer with standard scaling and model selection stage. create a pipeline with column transformer and also 
					                        cross validate to generalize model  
                                  
**stage_05_hyperparameter** tuning : We Tune the ppeline model parameters using RandomizedSearchCV to make model more generalize and more accurate.

**stage_06_pipeline** : We create ,fit/train and save the pipeline

**stage_07_prediction_pipeline** : Stage where our defined stock gets trigger extract the data using yfinance API while skipping the days when market is off. 
				Going through the whole pipeline and and create a column with 36 column where we make prediction whether to buy that stock or wait.
				
We also consider the situation if we stuck anywhere by **creating log files** for each and every steps for each stage
