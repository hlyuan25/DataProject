from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import numpy as np


def load_dataset():
    return make_classification(n_samples=1000)


def define_models():
    models = dict()
    models['KNN'] = KNeighborsClassifier()
    models['DTC'] = DecisionTreeClassifier()
    models['GNB'] = GaussianNB()
    models['SVM'] = SVC()
    models['LR'] = LogisticRegression()
    return models


def make_pipeline(model):
    steps = list()
    steps.append(('standardize', StandardScaler()))
    steps.append(('model', model))

    pipline = Pipeline(steps=steps)
    return pipline


def evaluate_single_model(X, y, model, folds):
    pipeline = make_pipeline(model)
    return cross_val_score(pipeline, X, y, cv=folds, scoring='accuracy')


def evaluate_models(X, y, models, folds=10):
    for name, model in models.items():
        scores = evaluate_single_model(X, y, model, folds)
        if scores is not None:
            score_mean = np.mean(scores)
            score_std = np.std(scores)
            print('%s: %f %f' % (name, score_mean, score_std))
        else:
            print('%s error.' % name)


X, y = load_dataset()
models = define_models()
evaluate_models(X, y, models, 10)
