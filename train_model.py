import pandas as pd
import xgboost as xgb
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import numpy as np
from create_games import games_columns


DROP_ARRAY = ['home_win', 'team_away', 'team_home', 'Unnamed: 0']
data = pd.read_excel('./Clean_Data/MLB_Games.xlsx')
print(data)
margin = data['home_win']
data.drop(DROP_ARRAY, axis=1, inplace=True)

data = data.values
data = data.astype(float)
max_acc = 0

feature_list =  [elem for elem in games_columns if elem not in DROP_ARRAY]

for x in tqdm(range(100)):
    x_train, x_test, y_train, y_test = train_test_split(data, margin, test_size=.1)
    
    train = xgb.DMatrix(x_train, label=y_train, feature_names=feature_list)
    test = xgb.DMatrix(x_test, label=y_test, feature_names=feature_list)
    param = {
            'max_depth': 6,
            'eta': 0.01,
            'objective': 'multi:softprob',
            'num_class': 2
        }
    epochs = 500

    model = xgb.train(param, train, epochs)
    predictions = model.predict(test)
    y = []

    for z in predictions:
        y.append(np.argmax(z))

    acc = round(accuracy_score(y_test, y), 3) * 100
    print(acc)
    print(model.get_score(importance_type='weight'))
    if acc > max_acc:
        model.save_model('./Models/XGBoost_{}%_ML-2.json'.format(acc))
        max_acc = acc