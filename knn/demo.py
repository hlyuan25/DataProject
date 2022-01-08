from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn import model_selection
import numpy as np


class DigitIdentify(object):

    def digit_identify(self):
        X, y = datasets.load_digits(return_X_y=True)
        knn = KNeighborsClassifier()
        X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.25)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        print(metrics.accuracy_score(y_test, y_pred))


if __name__ == '__main__':
    di = DigitIdentify()
    di.digit_identify()
