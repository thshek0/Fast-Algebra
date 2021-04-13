import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
from time import time
from Gaussian_Elimination import gauEli
from basic_function import genddm
from Gauss_Seidel_Iterative import gsi
from Jacobi_Iterative import jacobi
from sklearn.datasets import make_spd_matrix

numOfIter = 20
maxSize = 200
temp = np.zeros(numOfIter)
timeArr = np.zeros(maxSize + 1)

"""# Gaussian Elimination
for dim in range(1, maxSize+1):
    for i in range(numOfIter):
        aug = random.rand(dim, dim+1)

        # start program
        start = time()
        gauEli(dim, aug)
        temp[i] = time() - start

    timeArr[dim] = np.average(temp) * 1000
plt.plot(timeArr, label="Gaussian Elimination")"""


# Gauss-Seidel Iterative
for dim in range(1, maxSize+1):
    for i in range(numOfIter):
        A = genddm(dim)
        b = np.random.rand(dim)
        sol = np.zeros(dim)

        start = time()
        sol, fail = gsi(dim, A, b, sol, False)
        temp[i] = time() - start

    timeArr[dim] = np.average(temp) * 1000
plt.plot(timeArr, label="Gauss-Seidel Iterative")


# Jacobi Iterative
for dim in range(1, maxSize+1):
    for i in range(numOfIter):
        A = genddm(dim)
        b = np.random.rand(dim)
        sol = np.zeros(dim)

        start = time()
        sol, fail = jacobi(dim, A, b, sol, False)
        temp[i] = time() - start

    timeArr[dim] = np.average(temp) * 1000
plt.plot(timeArr, label="Jacobi Iterative")

# Cholesky Decomposition
for dim in range(1, maxSize + 1):
    for i in range(numOfIter):
        A = make_spd_matrix(dim)
        b = np.random.rand(dim)

        start = time()
        c, low = la.cho_factor(A)
        sol = la.cho_solve((c, low), b)
        temp[i] = time() - start

    timeArr[dim] = np.average(temp) * 1000
plt.plot(timeArr, label="Cholesky Decomposition")

# LU Decomposition
for dim in range(1, maxSize + 1):
    for i in range(numOfIter):
        A = np.random.rand(dim, dim)
        b = np.random.rand(dim)

        start = time()
        c, low = la.lu_factor(A)
        sol = la.lu_solve((c, low), b)
        temp[i] = time() - start

    timeArr[dim] = np.average(temp) * 1000
plt.plot(timeArr, label="LU Decomposition")

# plot graph
plt.title("Fast Linear Algebra (N=20)")
plt.xlabel("Size")
plt.ylabel("Time (ms)")
plt.xlim([1, maxSize])
plt.legend()
plt.grid()

plt.show()
