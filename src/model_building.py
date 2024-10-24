import pandas as pd
import os
import pickle
import yaml

from sklearn.ensemble import GradientBoostingClassifier

n_estimators=yaml.safe_load(open('params.yaml','r'))['model_building']['n_estimators']
lr=yaml.safe_load(open('params.yaml','r'))['model_building']['learning_rate']

#fetch
train_data=pd.read_csv('./data/features/train_bow.csv')
test_data=pd.read_csv('./data/features/test_bow.csv')

X_train=train_data.iloc[:,0:-1].values
y_train=train_data.iloc[:,-1].values

clf=GradientBoostingClassifier(n_estimators=50, learning_rate=lr)
clf.fit(X_train,y_train)

pickle.dump(clf,open('model.pkl','wb'))

