import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

name = ['sepal-length','sepal-width','petal-length','petal-width','class']
data = pd.read_csv('Data_8_9.csv',names=name)

x= data.iloc[:, :-1].values
y= data.iloc[:,4].values

xtrain,xtest,ytrain,ytest = train_test_split(x,y, test_size=20)

scaler = StandardScaler()
scaler.fit(xtrain)

xtrain = scaler.transform(xtrain)
xtest = scaler.transform(xtest)

classifier = KNeighborsClassifier(n_neighbors = 3)
classifier.fit(xtrain,ytrain)

y_pred = classifier.predict(xtest)

print("Tr.Ex\tActualLabel\tPredictedLabel")
for i in range(len(y_pred)):
	print(i+1,"\t",ytest[i],"\t\t",y_pred[i])

print("Confusion Matrix is")
print(confusion_matrix(ytest,y_pred))
print("Accuracy is :" , accuracy_score(ytest,y_pred)*100)
print("Classification Report:")
print(classification_report(ytest,y_pred))
