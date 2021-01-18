import numpy as np

import joblib
from matplotlib import pyplot

import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, recall_score,precision_score, classification_report, confusion_matrix
import collections
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import precision_recall_curve, roc_curve
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import label_binarize

np.random.seed(1337)  # for reproducibility

import xgboost as xgb

# import packages for hyperparameters tuning
from hyperopt import STATUS_OK, Trials, fmin, hp, tpe



X_train = np.load('../data/train/X_train.npy') 

Y_train = np.load('../data/train/Y_train.npy')

X_test = np.load('../data/test/set1/X_test.npy')

Y_test = np.load('../data/test/set1/Y_test.npy')

X_test2 = np.load('../data/test/set2/X_test2.npy')

Y_test2 = np.load('../data/test/set2/Y_test2.npy')


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)
X_test2 = scaler.fit_transform(X_test2)


print(X_train.shape)
print(Y_train.shape)

print(X_test.shape)
print(Y_test.shape)

print(X_test2.shape)
print(Y_test2.shape)


xgb_clf = xgb.XGBClassifier(learning_rate=0.1,
                          n_estimators=1000,
                          max_depth=5,
                          min_child_weight=1, gamma=0,
                          reg_alpha=0.01, n_jobs=-1,
                          subsample=0.5, colsample_bytree=0.5,
                          objective='multi:softmax', num_class=8)


