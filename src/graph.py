import numpy as np
import matplotlib.pyplot as plt
from numpy import random
from time import time
from Gaussian_Elimination import gauEli
from Gauss_Seidel_Iterative import gsi
from Jacobi_Iterative import jacobi


numOfIter = 50
maxSize = 50
temp = np.zeros(numOfIter)
timeArr = np.zeros(maxSize+1)


# Gaussian Elimination
for dim in range(1, maxSize+1):
    for i in range(numOfIter):
        aug = random.rand(dim, dim+1)

        # start program
        start = time()
        gauEli(dim, aug)
        end = time()

        temp[i] = end - start

    # change unit to ms
    timeArr[dim] = np.average(temp) * 1000

plt.plot(timeArr, label="Gaussian Elimination")


# Gauss-Seidel Iterative
for dim in range(1, maxSize+1):
    for i in range(numOfIter):
        # Make sure A is diagonally dominant
        A = random.rand(dim, dim)
        for x in range(dim):
            A[x][x] += dim
        A = (A - 0.5) * 100

        b = random.rand(dim)
        sol = np.zeros(dim)

        # start program
        start = time()
        sol, fail = gsi(dim, A, b, sol, False)
        end = time()

        temp[i] = end - start

    # change unit to ms
    timeArr[dim] = np.average(temp) * 1000

plt.plot(timeArr, label="Gauss-Seidel Iterative")

# Jacobi Iterative
for dim in range(1, maxSize+1):
    for i in range(numOfIter):
        # Make sure A is diagonally dominant
        A = random.rand(dim, dim)
        for x in range(dim):
            A[x][x] += dim
        A = (A - 0.5) * 100

        b = random.rand(dim)
        sol = np.zeros(dim)

        # start program
        start = time()
        sol, fail = jacobi(dim, A, b, sol, False)
        end = time()

        temp[i] = end - start

    # change unit to ms
    timeArr[dim] = np.average(temp) * 1000

plt.plot(timeArr, label="Jacobi Iterative")


# plot graph
plt.title("Fast Linear Algebra")
plt.xlabel("Size")
plt.ylabel("Time (ms)")
plt.xlim([1, maxSize])
plt.legend()
plt.grid()

plt.show()
