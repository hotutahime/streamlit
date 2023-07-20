import pandas as pd
import numpy as np
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from xgboost import plot_importance
from matplotlib import pyplot as plt

train_df = pd.read_csv("/Users/kato/jupyter/kaggle/house/kako.csv")
test_df = pd.read_csv("/Users/kato/jupyter/kaggle/house/mirai.csv")

X = train_df[["MSSubClass" , "LotFrontage" , "LotArea" , "MoSold" , "YrSold"]]
y = train_df["SalePrice"]
X = X.fillna(X.mean())

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, random_state=0)

gr_params = {
    "max_depth" : [5,10,15],
    "min_child_weight" : [5,10,15],
}

grid_search = GridSearchCV(XGBClassifier() , param_grid=gr_params, cv=5)

grid_search.fit(X_train , y_train)

print(grid_search.score(X_train , y_train))
print(grid_search.score(X_test , y_test))
print(grid_search.best_params_)

params = {
    "max_depth" : grid_search.best_params_["max_depth"],
    "min_child_weight" : grid_search.best_params_["min_child_weight"],
}

dtrain = xgb.DMatrix(X_train , label=y_train)
dtest = xgb.DMatrix(X_test , label=y_test)

model = xgb.train(params=params,
                 dtrain=dtrain,
                 num_boost_round=1000,
                 early_stopping_rounds=30,
                 evals=[(dtest , "test")])

print(model.best_ntree_limit)

test = test_df[["MSSubClass" , "LotFrontage" , "LotArea" , "MoSold" , "YrSold"]]
test = test.fillna(test.mean())

prediction = model.predict(xgb.DMatrix(test), ntree_limit = model.best_ntree_limit)

plot_importance(model)
plt.show()





