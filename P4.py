import numpy as np
from sklearn import preprocessing

x=np.array(([2,3],[4,5],[6,7],[8,9]),dtype=float)
y=np.array(([6],[20],[42],[72]),dtype=float)

x=preprocessing.normalize(x)
y=y/100

ni=2
nh=3
no=1

wh=np.random.uniform(size=(ni,nh))
bh=np.random.uniform(size=(1,nh))
wo=np.random.uniform(size=(nh,no))
bo=np.random.uniform(size=(1,no))

for i in range(10000):
	hval = x.dot(wh)+bh
	hact = 1/(1+np.exp(-hval))
	oval = hact.dot(wo)+bo
	oact = 1/(1+np.exp(-oval))

	eo = (y-oact)*oact*(1-oact)
	eh = (eo.dot(wo.T))*hact*(1-hact)
	wh += x.T.dot(eh)*0.8
	wo += hact.T.dot(eo)*0.8

for i in range(len(y)):
	print(y[i],"-->",oact[i])