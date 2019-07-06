# Week 1 projects

>All the details related to setup is provided [here](https://github.com/krishnayele/Machine-learning/blob/master/Python_Tutorial/README.md) in tutorial follow up.

### Description 

The mini project is find the gender of a person whose data given as height, weight, and BMI index can be detected.
The project uses three classification models

* DecisionTree
* Neural Network
* Ensemble 
  
The data is tested against a known data and the model that correctly predicts the gender is displayed.

It is a simple implementation of classification to get used to basic procedure

things to learn from this project

* How to split data from csv file
* basic working of "how to create Model"
* libraries used for different models

Models used and their library

 `
 from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
`