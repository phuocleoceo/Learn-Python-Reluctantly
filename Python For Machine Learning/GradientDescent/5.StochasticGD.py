# Tốn nhiều vòng lặp hơn hẳn nhưng kết quả thì lại tốt hơn nhiều
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
from random import randint


def grad(w):
    N = Xbar.shape[0]
    return 1/N * Xbar.T.dot(Xbar.dot(w) - y)


def cost(w):
    N = Xbar.shape[0]
    return 0.5/N*norm(y - Xbar.dot(w), 2)**2


def sgrad(w, Xbar_op, y_op):
    a = Xbar_op.dot(w) - y_op
    return (Xbar_op*a).reshape(2, 1)


def SGD(w_init, eta, loop=1000, esilon=1e-3):
    w = [w_init]
    N = Xbar.shape[0]
    for it in range(loop):
        random_i = randint(0, N-1)
        Xbar_op = Xbar[random_i]
        y_op = y[random_i]
        w_new = w[-1] - eta*sgrad(w[-1], Xbar_op, y_op)
        if norm(grad(w_new))/len(w_new) < esilon:
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
    w1, it1 = SGD(w_init, 0.1)
    print("SGD : ", w1[-1].T)
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
