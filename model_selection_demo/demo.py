from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from matplotlib import pyplot


X, y = load_iris(return_X_y=True)

models = []
models.append(('KNN', KNeighborsClassifier()))
models.append(('DTC', DecisionTreeClassifier()))
models.append(('GNB', GaussianNB()))
models.append(('SVM', SVC()))

result_set = []
names = []
for name, model in models:
    skf = StratifiedKFold(n_splits=10)
    cv_score = cross_val_score(model, X, y, cv=skf, scoring='accuracy')
    names.append(name)
    result_set.append(cv_score)
    print(name, cv_score)
    print('%s: %f (%f)(%f)' % (name, cv_score.mean(), cv_score.var(), cv_score.std()))


pyplot.boxplot(result_set, labels=names)
pyplot.show()
