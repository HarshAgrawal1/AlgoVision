
import pandas as pd
from io import TextIOWrapper
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import sklearn.datasets
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score


def LinearRegression(x_train,y_train,x_test,y_test):      # Linear Regression component
  from sklearn.linear_model import LinearRegression

  model=LinearRegression()
  model.fit(x_train,y_train)
  rmse_test = mean_squared_error(y_test,model.predict(x_test))**(0.5)
  return 1.96*rmse_test


def LogisticRegression(x_train,y_train,x_test,y_test):    #Logistic Regression component
  from sklearn.linear_model import LogisticRegression

  model = LogisticRegression(random_state=0)

  model.fit(x_train,y_train)
  return accuracy_score(y_test,model.predict(x_test))

def DecisionTree(x_train,y_train,x_test,y_test):          #Decision Tree component
  from sklearn.tree import DecisionTreeClassifier
  model = DecisionTreeClassifier()
  model.fit(x_train,y_train)
  return accuracy_score(y_test,model.predict(x_test))

def Svm(x_train,y_train,x_test,y_test):                   #SVM
  from sklearn.svm import SVC
  model = SVC()
  model.fit(x_train,y_train)
  return accuracy_score(y_test,model.predict(x_test))

def NB(x_train,y_train,x_test,y_test):                    #Naive Bayes
  from sklearn.naive_bayes import GaussianNB
  model = GaussianNB()
  model.fit(x_train,y_train)
  return accuracy_score(y_test,model.predict(x_test))


def KNN(x_train,y_train,x_test,y_test):                   #KNN
  from sklearn.neighbors import KNeighborsClassifier
  model = KNeighborsClassifier()
  model.fit(x_train,y_train)


  return accuracy_score(y_test,model.predict(x_test))


def RandomForest(x_train,y_train,x_test,y_test):                   #Random Forest
  from sklearn.ensemble import RandomForestClassifier
  model =RandomForestClassifier()
  model.fit(x_train,y_train)

  return accuracy_score(y_test,model.predict(x_test))






  

  
def train_model(csv_file,target_value):
  csv_file.seek(0)
  csv_file = TextIOWrapper(csv_file, encoding='cp1252')
  df=pd.read_csv(csv_file)
  y=df[target_value]
  df=df.drop(columns=[target_value])
  x=df
  lc=LabelEncoder()
  y=lc.fit_transform(y)
  for col in x.columns[:]:
    a=isinstance(x[col],object)
    if(a==True):
      x[col]=lc.fit_transform(x[col])
  x_train,x_test,y_train,y_test=train_test_split(x,y)
  sc=StandardScaler()
  sc.fit(x_train)
  sc.fit(x_test)

  algorithms=['Linear-Regression','Logistic Regression','Decision Tree','SVM','Naive Bayes','kNN','Random Forest']
  acc=[] 

  # LINEAR REGRESSION
  acc.append(LinearRegression(x_train,y_train,x_test,y_test))

  #LOGISTIC REGRESSION
  acc.append(LogisticRegression(x_train,y_train,x_test,y_test))

  #DECISION TREE
  acc.append(DecisionTree(x_train,y_train,x_test,y_test))

  # SVM
  acc.append(Svm(x_train,y_train,x_test,y_test))

  # Naive Bayes
  acc.append(NB(x_train,y_train,x_test,y_test))

  #KNN
  acc.append(KNN(x_train,y_train,x_test,y_test))

  # Random Forest
  acc.append(RandomForest(x_train,y_train,x_test,y_test))


  accuracy=0.00
  index=0

  for i in range(0,7):
    if(acc[i]>accuracy):
      index=i
      accuracy=acc[i]
  
  return algorithms[i],accuracy*100