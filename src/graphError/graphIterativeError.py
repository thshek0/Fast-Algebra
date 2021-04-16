import numpy as np
import matplotlib.pyplot as plt
from time import time
from basic_function import genddm
from Gauss_Seidel_Iterative_Restricted import gsi
from Jacobi_Iterative_Restricted import jacobi

numOfIter = 20
maxSize = 200

tempJac = np.zeros(numOfIter)
tempGSI = np.zeros(numOfIter)

errorJac = np.zeros(maxSize + 1)
errorGSI = np.zeros(maxSize + 1)

for dim in range(1, maxSize+1):
    for i in range(numOfIter):
        A = genddm(dim)
        b = np.random.rand(dim)
        sol = np.zeros(dim)

        sol, fail = jacobi(dim, A, b, sol, False, 5)
        estimate = np.dot(A, sol)
        error = 0
        for j in range(len(b)):
            error += abs(b[j] - estimate[j])
        tempJac[i] = error

        sol, fail = gsi(dim, A, b, sol, False, 5)
        estimate = np.dot(A, sol)
        error = 0
        for j in range(len(b)):
            error += abs(b[j] - estimate[j])
        tempGSI[i] = error

    
    errorJac[dim] = np.average(tempJac)
    errorGSI[dim] = np.average(tempGSI)
    
plt.plot(errorJac, label="Jacobi Iterative")
plt.plot(errorGSI, label="Gauss-Seidel Iterative")

# plot graph
plt.title("Error of Iterative Methods in 4 iterations")
plt.xlabel("Size")
plt.ylabel("Total Error")
plt.xlim([1, maxSize])
plt.legend()
plt.grid()

plt.show()
