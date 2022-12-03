import copy

import numpy as np
import pandas as pd
import xgboost as xgb
from colorama import Fore, Style, init, deinit



model = xgb.Booster()

model.load_model('./Models_Test/XGBoost_61.3%_ML-2.json')

test =  {
            'games_away': 100,
            'runs_away': .3,
            'ops_away': .6,

            'games_home': 100,
            'runs_home': 3.3,
            'ops_home': .9,
        }
print(type(test))
ml_prediction = model.predict(xgb.DMatrix(np.array([[6,3.3,.6,6,3.3,.6]])))
winner = int(np.argmax(ml_prediction))
print(winner)
winner_confidence = ml_prediction
print(winner_confidence)
winner_confidence = round(winner_confidence[0][1] * 100, 1)
print(winner_confidence)