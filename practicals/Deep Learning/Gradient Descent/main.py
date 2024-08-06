import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
m = 2000
n = 2

X = np.random.rand(m, n)
X[:, 0] = 1
true_theta = np.array([2, 3])
y = X.dot(true_theta) + np.random.randn(m) * 0.3

theta = np.zeros(n)
learning_rate = 0.01
num_iterations = 500

def compute_cost(X, y, theta):
    m = len(y)
    predictions = X.dot(theta)
    errors = predictions - y
    cost = (1 / (2 * m)) * np.sum(errors ** 2)
    return cost