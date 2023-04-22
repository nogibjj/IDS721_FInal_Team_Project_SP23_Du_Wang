# Packages
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score

# Read in data from zip file
zip_file_path = "/workspaces/IDS721_FInal_Team_Project_SP23_Du_Wang/00_source_data/heart_2020_cleaned.csv.zip"
# unzip the file and save it to the same directory as a csv
df = pd.read_csv(zip_file_path, compression='zip')
df.head()

# save the data to a csv file
df.to_csv('/workspaces/IDS721_FInal_Team_Project_SP23_Du_Wang/00_source_data/heart_2020_cleaned.csv', index=False)

# check the missing values
df.isnull().sum()
# HeartDisease        0
# BMI                 0
# Smoking             0
# AlcoholDrinking     0
# Stroke              0
# PhysicalHealth      0
# MentalHealth        0
# DiffWalking         0
# Sex                 0
# AgeCategory         0
# Race                0
# Diabetic            0
# PhysicalActivity    0
# GenHealth           0
# SleepTime           0
# Asthma              0
# KidneyDisease       0
# SkinCancer          0

# there is no missing values in the dataset
df.shape # (319795, 18)


# train test split
X = df.drop('HeartDisease', axis=1)
# encode Yes and No to 1 and 0
X = X.replace({'Yes': 1, 'No': 0})
# encode categorical variables into one-hot encoding
X = pd.get_dummies(X)
y = df['HeartDisease']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8886)


# Logistic Regression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))
# takes 5.9s to run, the accucracy is 0.92

# Confusion Matrix
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)
# [[57990   440]
#  [ 4971   558]]

# use random forest to see if we can get a better accuracy
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100, random_state=8886)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print('Accuracy of random forest classifier on test set: {:.2f}'.format(rf.score(X_test, y_test)))
# takes about 1 min, the accuracy is 0.90

# XGBoost
xgb = XGBClassifier()
xgb.fit(X_train, y_train)
y_pred = xgb.predict(X_test)
print('Accuracy of XGBoost classifier on test set: {:.2f}'.format(xgb.score(X_test, y_test)))