# The implementation of dynamic programming: optimal binary search trees: CLRS 15.5
# Given keys k1, k2, ..., kn k1<k2<kn, value of ki = i
# weights w1, w2, w3, ..., wn (search probabilities)
# e.g. w[i] = p[i], the probability of search for ki
# The goal is to find BST that minimizes sum(Wi * (depth(Ki) + 1))
# Solution:
# w(i, j) = w[i] + w[i+1] + ... + w[j]
# e(i, j) = wi if i = j
# e(i, j) = min ( (e(i, r-1) + e(r+1, j) + w(i, j) if i!=j

import numpy as np

def calculate_wij(w, i, j):
    wsum = 0
    if i > j:
        return 0
    if i == j:
        wsum = w[i]
    else:
        for m in range(i, j+1):
            wsum += w[m]
    return wsum


def optCost(w, i, j):
    wij = calculate_wij(w, i, j)
    min = float("inf")
    if i > j:
        return 0
    if i == j:
        return w[i]
    else:
        for r in range(i, j):
            cost = optCost(w, i, r - 1) + optCost(w, r + 1, j)
            if cost < min:
                min = cost
    return min + wij


def optimal_search_tree(k, w):
    return optCost(w, 1, len(k))


# Construct the k dictionary where Ki = i
# Construct the weights Wi for each Ki where weights stand for search probabilities
ki = {}
weights = {}
for key in range(1, 11):
    ki[key] = key
    weights[key] = np.random.randint(1, 10)
print(ki)
print(weights)
for key in weights:
    print([key, weights[key]])

print('The optimal binary search tress is: ' + str(optimal_search_tree(ki, weights)))