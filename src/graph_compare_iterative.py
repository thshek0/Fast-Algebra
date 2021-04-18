import numpy as np
import matplotlib.pyplot as plt
from time import time
from basic_function import genddm
from Gauss_Seidel_Iterative import gsi
from Jacobi_Iterative import jacobi

numOfIter = 20
maxSize = 200

tempJac = np.zeros(numOfIter)
tempGSI = np.zeros(numOfIter)

timeJac = np.zeros(maxSize + 1)
timeGSI = np.zeros(maxSize + 1)

for dim in range(1, maxSize+1):
    for i in range(numOfIter):
        A = genddm(dim)
        b = np.random.rand(dim)
        sol = np.zeros(dim)

        start = time()
        sol, fail = jacobi(dim, A, b, sol, False)
        tempJac[i] = time() - start

        start = time()
        sol, fail = gsi(dim, A, b, sol, False)
        tempGSI[i] = time() - start

    
    timeJac[dim] = np.average(tempJac) * 1000
    timeGSI[dim] = np.average(tempGSI) * 1000
    
plt.plot(timeJac, label="Jacobi Iterative")
plt.plot(timeGSI, label="Gauss-Seidel Iterative")

# plot graph
plt.title("Fast Linear Algebra")
plt.xlabel("Size")
plt.ylabel("Time (ms)")
plt.xlim([1, maxSize])
plt.legend()
plt.grid()

plt.show()
