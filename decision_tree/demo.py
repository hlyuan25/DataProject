from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn import model_selection
from six import StringIO
from sklearn.tree import export_graphviz
import pydotplus


class PredictDiabetes(object):
    @classmethod
    def predict_diabetes(cls):
        data_set = pd.read_csv('pima-indians-diabetes.csv')

        feature_columns = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']

        X = data_set[feature_columns]
        y = data_set.label

        print(X, y)

        dtc = DecisionTreeClassifier()
        dtc.fit(X, y)

        test_data = [10, 115, 0, 0, 0, 35.3, 0.134, 29]

        y_pred = dtc.predict(np.array(test_data).reshape(1, -1))
        print(y_pred)

        dot_data = StringIO()
        export_graphviz(dtc,
                        out_file=dot_data,
                        feature_names=feature_columns,
                        class_names=['0', '1'],
                        rounded=True,
                        filled=True,
                        special_characters=True)
        graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
        graph.write_pdf('decision_tree.pdf')

    @classmethod
    def metrics_diabetes(cls):
        data_set = pd.read_csv('pima-indians-diabetes.csv')

        feature_columns = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']

        X = data_set[feature_columns]
        y = data_set.label

        X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.25)

        dtc = DecisionTreeClassifier()
        dtc.fit(X_train, y_train)

        y_pred = dtc.predict(X_test)
        print(metrics.accuracy_score(y_test, y_pred))


if __name__ == '__main__':
    PredictDiabetes.predict_diabetes()
