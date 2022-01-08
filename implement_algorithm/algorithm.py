from math import sqrt
from sklearn.datasets import load_iris


class KNN(object):
    def calculate_distance(self, point1, point2):
        distance = 0.0
        for i in range(len(point1) - 1):
            distance += (point1[i] - point2[i]) ** 2
        return sqrt(distance)

    def find_neighbors(self, data_set, test_data):
        distances = []
        for train_data in data_set:
            distance = self.calculate_distance(train_data, test_data)
            distances.append((train_data, distance))
        distances.sort(key=lambda tup: tup[1])
        return distances[0][0]

    def predict(self, data_set, test_data):
        neighbor = self.find_neighbors(data_set, test_data)
        return neighbor[-1]

    def predict_results(self, train_set, test_set):
        results = []
        for test_data in test_set:
            y_pred = self.predict(train_set, test_data)
            results.append(y_pred)
        return results


if __name__ == '__main__':
    X, y = load_iris(return_X_y=True)
    # print(X)
    knn = KNN()
    test_data = [5.1, 3.5, 1.4, 0.3]
    distances = knn.find_neighbors(X, test_data)
    print(distances)
