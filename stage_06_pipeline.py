import logging
import os
import joblib
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from stage_03_preprocess_and_split import x_train , y_train , x , y
from stage_04_ct_and_model_selection import ct
from sklearn.model_selection import cross_val_score

STAGE = "PIPELINE CREATION" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


# creating pipeline
try:
    pipeline = Pipeline([
                        ('columnTransformer', ct),
                        ('model', RandomForestClassifier(
                                        bootstrap = True,
                                        max_depth = 60,
                                        max_features = 'auto',
                                        min_samples_leaf = 4,
                                        min_samples_split = 6,
                                        n_estimators = 19))                                                                                                           
                    ])

    accuracy_score = cross_val_score(pipeline, x, y, scoring='accuracy', cv=StratifiedKFold(n_splits=10), n_jobs=-1).mean()
    logging.info(accuracy_score)
except Exception as e:
    logging.exception(f'Error occured while creation of pipeline {e}')


# Pipeline fitting
try:
    pipeline.fit(x_train,y_train)
    logging.info(f'pipeline {pipeline} fit')
except Exception as e:
    logging.exception(f'Error occured while fitting pipeline {e}')


# Saving Pipeline
try:
    joblib.dump(pipeline, 'pipeline.joblib')
    logging.info(f'pipeline saved {pipeline}')
except Exception as e:
    logging.exception(f'Error occured while saving pipeline {e}')
