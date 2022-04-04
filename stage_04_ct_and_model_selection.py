import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns',5000)
import logging
import os
from stage_03_preprocess_and_split import x , y
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import StratifiedKFold
from imblearn.combine import SMOTETomek
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

STAGE = "CT AND MODEL SELECTION" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

# column Transformer
try:
    cols = []
    for i in range(0,36):
        cols.append(i)
    ct = ColumnTransformer(transformers=[
        ('ct1',StandardScaler(),cols)
    ],remainder='passthrough')
    logging.info(f'Column Transformer created : {ct}')
except Exception as e:
    logging.exception(f'Error occured while creating column transformer {e}')


# comparing different classification models using sklearn pipeline
try:
    models = [LogisticRegression(),
            DecisionTreeClassifier(),
            RandomForestClassifier(),
            AdaBoostClassifier(),
            GradientBoostingClassifier(),
            XGBClassifier(),
            KNeighborsClassifier(),
            SVC()]

    model_labels = [
            'model_lr',
            'model_dt',
            'model_rf',
            'model_ab',
            'model_gb',
            'model_xg',
            'model_knn',
            'model_svc'
        ]

    accuracy_mean_scores = []

    for model in models:
        pipeline = Pipeline([
                            ('columnTransformer', ct),
                            # ('resample', SMOTETomek()),
                            ('model', model)
        ])
        logging.info(f'Pipeline created for chossing model {pipeline}')
        accuracy_mean = cross_val_score(pipeline, x, y, cv=StratifiedKFold(n_splits=10), scoring='accuracy',n_jobs=-1).mean()
        accuracy_mean_scores.append(accuracy_mean)
        logging.info(accuracy_mean_scores)
        
except Exception as e:
    logging.exception(f'Error occured in pipeline for chossing model {e}')
