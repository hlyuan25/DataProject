import numpy


def tax(m):
    data = numpy.array([['养老保险', 0.08],
                        ['医疗保险', 0.02],
                        ['失业保险', 0.005],
                        ['住房公积金', 0.12]])

    rate = 0.0
    for i in range(len(data)):
        rate += float(data[i][1])

    n = m * rate
    if n > 7662:
        n = 7662

    return (m - n) - 3500
