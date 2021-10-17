import numpy as np

import matplotlib.pyplot as plt

np.random.seed(2)


def grad(w):
    N = Xbar.shape[0]
    return 1/N * Xbar.T.dot(Xbar.dot(w) - y)


def l(w):
    N = Xbar.shape[0]
    return 0.5/N*np.linalg.norm(Xbar.dot(w)-y, 2)**2


def myGradientDescent(w_init, grad, alpha, loop=1000, esilon=1e-4):
    w = [w_init]
    for i in range(loop):
        w_new = w[-1] - alpha*grad(w[-1])
        if np.linalg.norm(grad(w_new))/len(w_new) < esilon:
            break
        w.append(w_new)
    return (w, i)


if __name__ == '__main__':
    # dataset

    X = np.random.rand(1000, 1)

    y = 4 + 3 * X + 0.2 * np.random.randn(1000, 1)  # noise added

    # Building Xbar

    one = np.ones((X.shape[0], 1))

    Xbar = np.concatenate((one, X), axis=1)

    # Gradient descent

    w_init = np.array([[2], [1]])

    (w1, it1) = myGradientDescent(w_init, grad, 0.01)

    print(' Phương pháp GradientDescent: w = ',
          w1[-1].T, ',\n after %d iterations.' % (it1+1), ',\n l = %f ' % l(w1[-1]))

    # Linear regression

    A = np.dot(Xbar.T, Xbar)

    b = np.dot(Xbar.T, y)

    w_lr = np.dot(np.linalg.pinv(A), b)

    print('Phương pháp nghịch đảo: w = ', w_lr.T)

    # Display result

    #w = w_lr

    w = w1[-1]

    w_0 = w[0][0]

    w_1 = w[1][0]

    x0 = np.linspace(0, 1, 2, endpoint=True)

    y0 = w_0 + w_1 * x0

    # Draw the fitting line

    plt.plot(X.T, y.T, 'b.')  # data

    plt.plot(x0, y0, 'y', linewidth=2)  # the fitting line

    plt.axis([0, 1, 0, 10])

    plt.show()
