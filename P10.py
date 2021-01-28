import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def kernel(point,xmat,k):
	m=np.shape(xmat)[0]
	weights = np.mat(np.eye(m))
	for j in range(m):
		diff = point - X[j]
		weights[j,j] = np.exp((diff*diff.T)/(-2*k**2))
	return weights

def  LW(point,xmat,ymat,k):
	weight = kernel(point,xmat,k)
	W = (xmat.T*(weight*xmat)).I*(X.T*(weight*ymat.T))
	return W

def LWR(xmat,ymat,k):
	m = np.shape(xmat)[0]
	ypred = np.zeros(m)
	for i in range(m):
		ypred[i] = xmat[i] * LW(xmat[i],xmat,ymat,k)
	return ypred

def graphplot(X,ypred):
	sortindex = X[:,1].argsort(0)
	xsort = X[sortindex][:,0]
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.scatter(bill,tip,color='blue',s=5)
	ax.plot(xsort[:,1],ypred[sortindex],color='red',linewidth=2)
	plt.show()

data = pd.read_csv('Data10.csv')
bill = np.array(data.total_bill)
tip = np.array(data.tip)

mbill = np.mat(bill)
mtip = np.mat(tip)

m = np.shape(mbill)[1]
one = np.mat(np.ones(m))

X = np.hstack((one.T,mbill.T))

ypred = LWR(X,mtip,0.8)
graphplot(X,ypred)