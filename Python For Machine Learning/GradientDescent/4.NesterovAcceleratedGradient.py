import numpy as np
import matplotlib.pyplot as plt


def grad(x):
    return 2*x + 10*np.cos(x)


def cost(x):
    return x**2 + 10*np.sin(x)


def NAG(theta_init, alpha=0.1, beta=0.9, Loop=1000, esilon=1e-3):
    theta = [theta_init]
    v_old = np.zeros_like(theta_init)
    for it in range(Loop):
        v_new = beta*v_old + alpha*grad(theta[-1]-beta*v_old)
        theta_new = theta[-1] - v_new
        if np.abs(grad(theta_new)) < esilon:
            break
        theta.append(theta_new)
        v_old = v_new
    return theta, it


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

    x1, it1 = myGD1(5, 0.1)
    print("GD x =", x1[-1], ", cost = ", cost(x1[-1]))
    print("after", it1, "iterations")
    plt.plot(x1[-1], cost(x1[-1]), 'b X')

    x, it = NAG(5, 0.1, 0.9)
    print("Nesterov x =", x[-1], ", cost = ", cost(x[-1]))
    print("after", it, "iterations")
    plt.plot(x[-1], cost(x[-1]), 'b X')

    plt.show()
