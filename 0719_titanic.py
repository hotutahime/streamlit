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

train_df = pd.read_csv("/Users/kato/jupyter/kaggle/titanic/titanic/train.csv")
test_df = pd.read_csv("/Users/kato/jupyter/kaggle/titanic/titanic/test.csv")

X = train_df.drop(["Survived" , "PassengerId" , "Name" , "Ticket" , "Cabin"] , axis=1)
y = train_df["Survived"]

for i in ["Sex" , "Embarked"]:
    lbl = LabelEncoder()
    X[i] = lbl.fit_transform(list(X[i].values))

X = X.fillna(X.mean())

X_train , X_test , y_train , y_test = train_test_split(X , y , shuffle=True , random_state=0)

gr_params = {
    "max_depth" : [5,10,15],
    "min_child_weight" : [5,10,15],
    "subsample" : [0.2,0.6,1.0],
    "colsample_bytree" : [0.2,0.6,1.0],
    "eta" : [0.2,0.5,1.0]
}

grid_search = GridSearchCV(XGBClassifier() , param_grid=gr_params, cv=5)
grid_search.fit(X_train , y_train)

print(grid_search.score(X_train , y_train))
print(grid_search.score(X_test , y_test))
print(grid_search.best_params_)

params = {
    "max_depth" : grid_search.best_params_["max_depth"],
    "min_child_weight" : grid_search.best_params_["min_child_weight"],
    "subsample" : grid_search.best_params_["subsample"],
    "colsample_bytree" : grid_search.best_params_["colsample_bytree"],
    "eta" : grid_search.best_params_["eta"],
    "tree_method" : "exact",
    "objective" : "binary:logistic",
    "eval_metric" : "error"
}

dtrain = xgb.DMatrix(X_train , label=y_train)
dtest = xgb.DMatrix(X_test , label=y_test)

model = xgb.train(params=params,
                 dtrain=dtrain,
                 num_boost_round=10000,
                 early_stopping_rounds=500,
                 evals=[(dtest , "test")])

print(model.best_ntree_limit)

test = test_df.drop(["PassengerId", "Name" , "Ticket" , "Cabin"] , axis=1)

for j in ["Sex" , "Embarked"]:
    lbl = LabelEncoder()
    test[j] = lbl.fit_transform(list(test[j].values))

test = test.fillna(test.mean())

prediction = model.predict(xgb.DMatrix(test), ntree_limit = model.best_ntree_limit)

ID = test_df["PassengerId"]
prediction

prediction = np.where(prediction < 0.5 , 0 , 1)
prediction

plot_importance(model)
plt.show()

submission = pd.DataFrame({
    "PassengerId":ID,
    "Survived":prediction
})


submission.to_csv("/Users/kato/jupyter/kaggle/titanic/titanic/0719_2.csv" , index=False)








