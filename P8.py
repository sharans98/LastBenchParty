import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.mixture import GaussianMixture

iris = datasets.load_iris()
x=pd.DataFrame(iris.data)
x.columns=['SL','SW','PL','PW']
xnorm = preprocessing.normalize(x)
y=pd.DataFrame(iris.target)
y.columns=['Targets']

model = KMeans(n_clusters=3)
model.fit(xnorm)

gmm = GaussianMixture(n_components=3)
gmm.fit(xnorm)
gmm_y = gmm.predict(xnorm)

plt.figure(figsize=(10,10))
colormap = np.array(['blue','red','green'])

plt.subplot(2,2,1)
plt.scatter(x.PL,x.PW, c=colormap[y.Targets.values],s=100)

plt.subplot(2,2,2)
plt.scatter(x.PL,x.PW, c=colormap[model.labels_],s=100)

plt.subplot(2,2,3)
plt.scatter(x.PL,x.PW, c=colormap[gmm_y],s=300)

plt.show()

