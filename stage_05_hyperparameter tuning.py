from sklearn.model_selection import RandomizedSearchCV
import logging
import os
import numpy as np
from stage_03_preprocess_and_split import x_train , y_train
from stage_04_ct_and_model_selection import ct
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold

STAGE = "HYPERPARAMETER TUNING" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

# for rf
n_estimators = [int(x) for x in np.linspace(start = 1, stop = 20, num = 20)]  # number of trees in the random forest
max_features = ['auto', 'sqrt']                                               # number of features in consideration at every split
max_depth = [int(x) for x in np.linspace(10, 120, num = 12)]                  # maximum number of levels allowed in each decision tree
min_samples_split = [2, 6, 10]                                                # minimum sample number to split a node
min_samples_leaf = [1, 3, 4]                                                  # minimum sample number that can be stored in a leaf node
bootstrap = [True, False]                                                     # method used to sample data points

params = {
      'model__n_estimators': n_estimators,
      'model__max_features': max_features,
      'model__max_depth': max_depth,
      'model__min_samples_split': min_samples_split,
      'model__min_samples_leaf': min_samples_leaf,
      'model__bootstrap': bootstrap
        }
logging.info(f'Params for random forest defined : {params}')
    
try:
    pipeline = Pipeline([
                        ('columnTransformer', ct),
                        ('model', RandomForestClassifier())
                        ])

    random_search = RandomizedSearchCV(pipeline,param_distributions=params,scoring='accuracy',n_jobs=-1,cv=StratifiedKFold(n_splits=10))
    random_search.fit(x_train, y_train)

    logging.info(random_search.best_params_)
    logging.info(random_search.best_score_)

except Exception as e:
    logging.exception(f'Error occured while extracting best params {e}')

    