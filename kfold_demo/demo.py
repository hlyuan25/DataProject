import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

# read data from csv
data_set = pd.read_csv('pima-indians-diabetes.csv')
feature_columns = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']
X = data_set[feature_columns]
y = data_set.label

# data processing
mms = MinMaxScaler()
X_new = mms.fit_transform(X)

# model selection
model = LogisticRegression(solver='lbfgs') #mean: 0.68  var: 0.02  std: 0.12
#model = RandomForestClassifier()          #mean: 0.63  var: 0.02  std: 0.13

# cross validation/strategy
kfold = KFold(n_splits=10)

# estimation
cv_score = cross_val_score(model, X_new, y, cv=kfold)

print('mean: %.2f  var: %.2f  std: %.2f' % (cv_score.mean(), cv_score.var(), cv_score.std()))
