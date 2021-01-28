import csv

dataset = list(csv.reader(open('train.csv')))
attributes = dataset[0]
dataset.remove(attributes)
attributes.remove('enjoy')
target = ['Yes','Yes','No','Yes']
hypothesis = ["0"] * len(attributes)

for i in range(len(target)):
	if target[i]=='Yes':
		for j in range(len(attributes)):
			if hypothesis[j]=='0':
				hypothesis[j]=dataset[i][j]
			if hypothesis[j]!=dataset[i][j]:
				hypothesis[j]="?"
	print("Hypothesis is -> ",hypothesis)
print("Final Hypothesis is==>",hypothesis)