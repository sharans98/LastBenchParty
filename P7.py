import pandas as pd
import numpy as np
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

data =pd.read_csv('Data7.csv')
data = data.replace('?',np.nan)

model = BayesianModel([('age','trestbps'),('age','fbs'),('sex','trestbps'),('sex','fbs'),('exang','trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'),('heartdisease','chol'),('heartdisease','restecg'),('heartdisease','thalach')])

model.fit(data,estimator = MaximumLikelihoodEstimator)
data_infer = VariableElimination(model)

q = data_infer.query(variables=['heartdisease'],evidence={'age':20})
print(q)
