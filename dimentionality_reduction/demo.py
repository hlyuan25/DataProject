from sklearn.datasets import make_classification
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from matplotlib import pyplot


def load_dataset():
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=15, n_redundant=5)
    return X, y


def dimensionality_reduction(X):
    pca = PCA(n_components=5)
    X_new = pca.fit_transform(X)
    return X_new


def define_model():
    models = dict()
    for i in range(1, 21):
        steps = [('pca', PCA(n_components=i)), ('model', LogisticRegression())]
        models[i] = Pipeline(steps=steps)
    return models


def evaluate_model(model, X, y):
    rskf = RepeatedStratifiedKFold(n_splits=10, n_repeats=3)
    cv_score = cross_val_score(model, X, y, scoring='accuracy', cv=rskf)
    print(cv_score)
    print('mean: %.3f  std:%.3f' % (cv_score.mean(), cv_score.std()))
    return cv_score


if __name__ == '__main__':
    X, y = load_dataset()
    models = define_model()
    names = []
    results = []
    for name, model in models.items():
        cv_score = evaluate_model(model, X, y)
        names.append(name)
        results.append(cv_score)
    pyplot.boxplot(results, labels=names)
    pyplot.show()
