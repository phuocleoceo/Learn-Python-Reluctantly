import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
from numpy.random import permutation


def grad(w, Xbar, y):
    N = Xbar.shape[0]
    return 1/N * Xbar.T.dot(Xbar.dot(w) - y)


def cost(w):
    N = Xbar.shape[0]
    return 0.5/N*norm(y - Xbar.dot(w), 2)**2


def MiniBatch(w_init, eta, quantity, loop=1000, esilon=1e-3):
    w = [w_init]
    N = Xbar.shape[0]
    for it in range(loop):
        random_i = permutation(N)
        Xbar_rand = Xbar[random_i]
        y_rand = y[random_i]
        for i in range(0, N, quantity):
            Xbar_mini = Xbar_rand[i:i+quantity]
            y_mini = y_rand[i:i+quantity]
            w_new = w[-1] - eta*grad(w[-1], Xbar_mini, y_mini)
            if norm(grad(w_new, Xbar_mini, y_mini))/len(w_new) < esilon:
                return w, it
            w.append(w_new)
    return w, it


if __name__ == "__main__":
    # dataset
    X = np.random.rand(1000, 1)
    y = 4 + 3 * X + .2 * np.random.randn(1000, 1)

    # Building Xbar
    one = np.ones((X.shape[0], 1))
    Xbar = np.concatenate((one, X), axis=1)

    w_init = np.array([[2], [1]])
    w1, it1 = MiniBatch(w_init, 0.1, 50)
    print("MiniBatch : ", w1[-1].T)
    print("after : ", it1+1, "iterations")
    print("Cost :", cost(w1[-1]))

    # Linear regression
    A = np.dot(Xbar.T, Xbar)
    b = np.dot(Xbar.T, y)
    w_lr = np.dot(np.linalg.pinv(A), b)
    print('Phương pháp nghịch đảo: w = ', w_lr.T)

    # Display result
    w = w1[-1]
    w_0 = w[0][0]
    w_1 = w[1][0]
    x0 = np.linspace(0, 1, 2, endpoint=True)
    y0 = w_0 + w_1 * x0
    # Draw the fitting line
    plt.plot(X.T, y.T, 'b.')
    plt.plot(x0, y0, 'y', linewidth=2)
    plt.axis([0, 1, 0, 10])
    plt.show()
