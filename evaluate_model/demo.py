from csv import reader
from random import randrange
from implement_algorithm.algorithm import KNN
import numpy as np


def load_data(path):
    data_set = []
    with open(path, 'r') as file:
        lines = reader(file)
        for line in lines:
            if not line:
                continue
            data_set.append(line)
    return data_set


def convert_to_float(data_set):
    for data in data_set:
        for i in range(len(data) - 1):
            data[i] = float(data[i].strip())


def kfold_split(data_set, n_folds):
    data_set_copy = list(data_set)
    data_set_split = list()
    fold_size = int(len(data_set) / n_folds)
    for i in range(n_folds):
        fold = list()
        while len(fold) < fold_size:
            index = randrange(len(data_set_copy))
            fold.append(data_set_copy.pop(index))
        data_set_split.append(fold)
    return data_set_split


def accuracy_score(y_true, y_pred):
    correct = 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            correct += 1
    return correct / len(y_true)


def evaluate_algorithm(data_set, model, n_folds):
    folds = kfold_split(data_set, n_folds)
    scores = []
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])
        test_set = []
        for row in fold:
            row_copy = list(row)
            row_copy[-1] = None
            test_set.append(row_copy)
        predicted = model.predict_results(train_set, test_set)
        actual = [row[-1] for row in fold]
        score = accuracy_score(actual, predicted)
        scores.append(score)
    return scores


if __name__ == '__main__':
    data_set = load_data('raw-data.csv')
    convert_to_float(data_set)
    # print(data_set)
    # print(kfold_split(data_set, 5))
    knn = KNN()
    cv_scores = evaluate_algorithm(data_set, knn, n_folds=5)

    print(np.mean(cv_scores))
