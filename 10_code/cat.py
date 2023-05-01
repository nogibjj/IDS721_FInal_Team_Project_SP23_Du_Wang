import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def preprocess_data(data_path):
    # Read in data from csv file
    df = pd.read_csv(data_path)
    
    # Encode Yes and No to 1 and 0
    df = df.replace({'Yes': 1, 'No': 0})
    
    # Encode categorical variables into one-hot encoding
    df = pd.get_dummies(df)
    
    # Split data into features and target
    X = df.drop('HeartDisease', axis=1)
    y = df['HeartDisease']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8886)
    
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    # Create a decision tree classifier with max_depth=3
    clf = DecisionTreeClassifier(max_depth=3, random_state=8886)
    
    # Train the model on the training set
    clf.fit(X_train, y_train)
    
    return clf

def evaluate_model(clf, X_test, y_test):
    # Use the trained model to make predictions on the testing set
    y_pred = clf.predict(X_test)
    
    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: {:.2f}".format(accuracy))
    
    # Calculate the confusion matrix of the model
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:\n", cm)

if __name__ == "__main__":
    # Set the path to the data file
    data_path = "/workspaces/IDS721_FInal_Team_Project_SP23_Du_Wang/00_source_data/heart_2020_cleaned.csv"
    
    # Preprocess the data
    X_train, X_test, y_train, y_test = preprocess_data(data_path)
    
    # Train the model
    clf = train_model(X_train, y_train)
    
    # Evaluate the model
    evaluate_model(clf, X_test, y_test)
