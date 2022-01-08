from sklearn.cluster import KMeans


def load_data(path):
    file = open(path, 'r')
    lines = file.readlines()
    customer_names = []
    data_set = []
    for line in lines:
        items = line.strip().split(',')
        customer_names.append(items[0])
        data_set.append([float(items[i]) for i in range(1, len(items))])
    return data_set, customer_names


if __name__ == '__main__':
    data_set, customer_names = load_data('customer.txt')
    kmeans = KMeans(n_clusters=3)
    lables = kmeans.fit_predict(data_set)
    print(customer_names)
    print(lables)

    customer_clusters = [[],[],[]]
    for i in range(len(customer_names)):
        customer_clusters[lables[i]].append(customer_names[i])

    for i in range(len(customer_clusters)):
        print(customer_clusters[i])
