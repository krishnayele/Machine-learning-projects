from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

import pandas as pd 
import numpy as np 
#[height, weight, BMI index]
#input the data 
#csv 500_Person_Gender_Height_Weight_Index.csv

data = pd.read_csv("500_Person_Gender_Height_Weight_Index.csv")
Y= data.Gender 
X = data.drop('Gender',axis = 1)


#the figure of person whose sex is to be predicted
_value = [[167,75,3]]


#testing through Decision Tree
clf1 = tree.DecisionTreeClassifier()

clf1 = clf1.fit(X, Y)

prediction1 = clf1.predict(_value)

print("Result through Decision Tree : ", prediction1)

#testing using Neural network
clf2 = MLPClassifier(alpha=1, max_iter=1000)
clf2 = clf2.fit(X, Y)
prediction2 = clf2.predict(_value)

print("Result by Neuaral Network :    ", prediction2)

#testing using Random Forest classifier
clf3 = RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)
clf3 = clf3.fit(X, Y)
prediction3 = clf3.predict(_value)

print("Result by Random forest generator: ", prediction3)

#testing using ADABooST

clf4 = AdaBoostClassifier()
clf4.fit(X,Y)
prediction4 = clf4.predict(_value)

print("Result by Ada Boost    : ", prediction4)
