import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler

data_set = pd.read_csv('pima-indians-diabetes.csv')
feature_columns = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']
X = data_set[feature_columns]
y = data_set.label

mms = MinMaxScaler()
X_new = mms.fit_transform(X)
np.set_printoptions(precision=3)
print(X_new)
