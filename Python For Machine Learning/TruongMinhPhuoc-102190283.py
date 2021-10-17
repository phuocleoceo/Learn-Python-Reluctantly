# Gradient Descent với hàm nhiều biến cho bài toán Linear Regression
# giúp xác định hàm mất mát nhỏ nhất có thể thông qua việc tìm các điểm cực tiểu cục bộ
# và xem đó gần như là giá trị nhỏ nhất có thể chấp nhận được

# Ngoài ra có thể áp dụng vào bài toán K-means Clustering để xử lý hàm mất mát tương tự như Linear Regression
# và tối ưu các bài toán SVD, Spectral Clustering, Non-Negative Matrix Factorization, Page Rank,...
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm

np.random.seed(2)


def grad(w):
    N, _ = np.shape(Xbar)
    return 1/N * Xbar.T.dot(Xbar.dot(w) - Y)


def l(w):
    N, _ = np.shape(Xbar)
    return 0.5/N*norm(Xbar.dot(w)-Y, 2)**2


def myGradientDescent(w_init, grad, alpha, loop=1000, esilon=1e-4):
    w = [w_init]
    for i in range(loop):
        w_new = w[-1] - alpha*grad(w[-1])
        if norm(grad(w_new))/len(w_new) < esilon:
            break
        w.append(w_new)
    return (w, i)


if __name__ == '__main__':
    # Random dữ liệu
    X = np.random.rand(1000, 1)

    # Tạo y với sự chênh lệch so với đường thẳng gốc
    Y = 5 + 3 * X + 0.2 * np.random.randn(1000, 1)

    # Tạo Xbar
    one = np.ones((np.shape(X)[0], 1))

    Xbar = np.concatenate((one, X), axis=1)

    # Gradient descent
    w_init = np.array([[2], [1]])

    (w1, it1) = myGradientDescent(w_init, grad, 0.01)

    print("GradientDescent: w = ", w1[-1].T, "after", (it1+1), "iterations.")
    print("l = ", l(w1[-1]))

    # Linear regression

    w = w1[-1]

    w_0 = w[0][0]

    w_1 = w[1][0]

    x0 = np.array([0, 1])

    y0 = w_0 + w_1 * x0

    plt.plot(X.T, Y.T, 'b.')  # Vẽ tập hợp điểm

    plt.plot(x0, y0, 'y', linewidth=2)  # Vẽ đường thằng y=ax+b với x1=0 x2=1

    plt.axis([0, 1, 0, 10])

    plt.show()
