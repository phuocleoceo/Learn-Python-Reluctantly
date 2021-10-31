import numpy as np
from numpy.linalg import norm, pinv
from numpy.random import permutation, rand
import matplotlib.pyplot as plt

np.random.seed(2)


def cost(w):
    N = Xbar.shape[0]
    return 0.5/N*norm(Xbar.dot(w)-y, 2)**2


# single point gradient
def sgrad(w, i, rd_id):
    true_i = rd_id[i]
    xi = Xbar[true_i, :]
    yi = y[true_i]
    a = xi.dot(w) - yi
    return (xi*a).reshape(2, 1)


def SGD(w_init, eta, esilon=1e-3):
    w = [w_init]
    w_last_check = w_init
    iter_check_w = 10
    N = X.shape[0]
    count = 0
    for it in range(10):
        rd_id = permutation(N)
        for i in range(N):
            count += 1
            g = sgrad(w[-1], i, rd_id)
            w_new = w[-1] - eta*g
            w.append(w_new)
            if count % iter_check_w == 0:
                w_this_check = w_new
                if norm(w_this_check - w_last_check)/len(w_init) < esilon:
                    return w, it
                w_last_check = w_this_check
    return w, it


if __name__ == '__main__':
    # dataset
    X = rand(1000, 1)
    y = 4 + 3 * X + 0.2 * np.random.randn(1000, 1)

    # Building Xbar
    one = np.ones((X.shape[0], 1))
    Xbar = np.concatenate((one, X), axis=1)

    # Gradient descent
    w_init = np.array([[2], [1]])
    w1, it1 = SGD(w_init, 0.01)
    print("StochasticGradientDescent: w = ", w1[-1].T)
    print("after", it1+1, "iterations")
    print("cost = ", cost(w1[-1]))

    # Linear regression
    A = np.dot(Xbar.T, Xbar)
    b = np.dot(Xbar.T, y)
    w_lr = np.dot(pinv(A), b)
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
