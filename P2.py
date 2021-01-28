import numpy as np
import pandas as pd

data = pd.DataFrame(pd.read_csv('candi.csv'))
concepts = np.array(data.iloc[:,0:-1])
target = np.array(data.iloc[:,-1])

Sh = concepts[0].copy()
Gh = [['?' for i in range(len(Sh))] for i in range(len(Sh))]

for i,h in enumerate(concepts):
	if target[i]=='yes':
		for x in range(len(Sh)):
			if (h[x]!=Sh[x]):
				Sh[x] = '?'
				Gh[x][x] = '?'
	if target[i]=='no':
		for x in range(len(Sh)):
			if h[x]!=Sh[x]:
				Gh[x][x]=Sh[x]
			else:
				Gh[x][x]='?'
	print('Specific->',Sh)
	print('General-->',Gh)

Gh.remove(['?','?','?','?','?','?'])
Gh.remove(['?','?','?','?','?','?'])
Gh.remove(['?','?','?','?','?','?'])
Gh.remove(['?','?','?','?','?','?'])
print("Final Generalisation==>>",Gh)
print("Final Specification===>>",Sh)
