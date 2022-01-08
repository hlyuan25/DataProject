import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

data_set = pd.read_csv('pima-indians-diabetes.csv')
feature_columns = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']
X = data_set[feature_columns]
y = data_set.label

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
lr = LogisticRegression(solver='liblinear')
lr.fit(X_train, y_train)

# finalize model in disk
filename = 'finalized_model.ml'
# pickle.dump(lr, open(filename, 'wb'))

# load model from disk
loaded_model = pickle.load(open(filename, 'rb'))
y_pred = loaded_model.predict(X_test)
print(y_pred)

