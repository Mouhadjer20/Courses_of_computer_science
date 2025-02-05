import numpy as np

def gradient_descent(x, y, max_iteration=1000):
    tita_0 = tita_1 = 0
    m = len(x)
    alpha = 0.01

    for i in range(max_iteration):
        y_predicted = tita_1 * x + tita_0
        cost = (1/(m))* sum([val**2 for val in (y_predicted-y)])
        print(f"tita_0 = {tita_0}, tita_1 = {tita_1}, y_pread = {y_predicted}, cost = {cost} iteration = {i}")

        integral_0 = -(2/m) * sum(y - y_predicted)
        integral_1 = -(2/m) * sum(x*(y - y_predicted))

        tita_0 -= alpha * integral_0
        tita_1 -= alpha * integral_1

gradient_descent(np.array([1, 2, 3, 4, 5]), np.array([5, 7, 9, 11, 13]))