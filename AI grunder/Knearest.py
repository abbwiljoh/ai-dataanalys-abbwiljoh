import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
import warnings
style.use('fivethirtyeight')

dataset = {'k': [[2, 5], [4, 1], [6, 5]],
           'g': [[3, 2], [6, 3], [4, 5]],
           'r': [[5, 5], [7, 7], [8, 6]]}
new_feature = [4, 3]


def knearest(data, predict, k=3):
    if len(data) <= k:
        warnings.warn("K is set to a value less than total groups!")
    distance = []
    for group in data:
        for feature in data[group]:
            euclidian_distance = np.linalg.norm(
                np.array(feature) - np.array(predict))
            distance.append([euclidian_distance, group])
    votes = [i[1] for i in sorted(distance)[:k]]
    votesResult = Counter(votes).most_common(1)[0][0]
    return votesResult


result = knearest(dataset, new_feature)

print(result)

[[plt.scatter(ii[0], ii[1], color=i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_feature[0], new_feature[1], s=100)

plt.show()
