# Jacobi Iterative
import numpy as np
from basic_function import inputMatrix, printMatrix

def jacobi(dim, A, b, sol, mes, limit):
    fail = False
    for it_count in range(limit):
        if it_count != 0 and mes:
            print("Iteration " + str(it_count) + ": " + str(sol))
        sol_new = np.zeros(dim)
        for i in range(dim):
            s = np.dot(A[i,:], sol)
            s = s - A[i,i] * sol[i]
            sol_new[i] = (b[i] - s) / A[i][i]

        # update value of sol
        sol = sol_new

    return sol, fail


def main():
    dim = int(input("What is the number of unknown variables? "))
    A, b = inputMatrix(dim)
    sol = np.zeros(dim)
    printMatrix("Inputted matrix", dim, A, b)
    sol, fail = jacobi(dim, A, b, sol, True, 5)

    # print message
    print("Solution:" + str(sol))
    print("Error:" + str(np.dot(A, sol) - b))


if __name__ == "__main__":
    main()
