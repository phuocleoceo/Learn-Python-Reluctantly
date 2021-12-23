import numpy as np
import matplotlib.pyplot as plt


def grad(x):  # f'(x)

    return 2*x + 10*np.cos(x)


def cost(x):  # f(x) x^2 + 10x sin(x)

    return x**2 + 10*np.sin(x)


def GD_momentum(theta_init, alpha=0.1, beta=0.9, Loop=1000, esilon=1e-3):

    theta = [theta_init]

    v_old = np.zeros_like(theta_init)

    for it in range(Loop):

        v_new = beta*v_old + alpha*grad(theta[-1])  # vt

        theta_new = theta[-1] - v_new
        if np.abs(grad(theta_new)) < esilon:
            break
        theta.append(theta_new)

        v_old = v_new

    return (theta, it)


def myGD1(x0, alpha=0.1, gra=1e-3, loop=1000):

    x = [x0]

    for it in range(loop):

        x_new = x[-1] - alpha*grad(x[-1])

        if abs(grad(x_new)) < gra:

            break

        x.append(x_new)

    return (x, it)


if __name__ == '__main__':

    X = np.linspace(-5, 5, 200)

    y = cost(X)

    plt.plot(X.T, y.T, 'r.')

    plt.axis([-5, 5, -10, 15])

    (x1, it1) = myGD1(5, 0.1)

    print('GD_Solution x1 = %f, cost = %f, obtained after %d iterations' %
          (x1[-1], cost(x1[-1]), it1))

    plt.plot(x1[-1], cost(x1[-1]), 'b X')

    (x2, it2) = GD_momentum(5, 0.1, beta=0.9)

    print('Momentum_Solution x2 = %f, cost = %f, obtained after %d iterations' % (
        x2[-1], cost(x2[-1]), it2))

    plt.plot(x2[-1], cost(x2[-1]), 'b X')

    plt.show()
