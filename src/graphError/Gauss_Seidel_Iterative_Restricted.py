# improved version of Jacobi Iterative
# condition: converge system, i.e. diagonally dominant
# not suitable for all systems, e.g. [1,2,3][4,5,6]
import numpy as np
from basic_function import inputMatrix, printMatrix


def gsi(dim, A, b, sol, mes, limit):
    fail = False
    for it_count in range(limit):
        if it_count != 0 and mes:
            print("Iteration " + str(it_count) + ": " + str(sol))
        sol_new = np.zeros(dim)

        for i in range(dim):
            s1 = np.dot(A[i, :i], sol_new[:i])
            s2 = np.dot(A[i, i + 1:], sol[i + 1:])
            sol_new[i] = (b[i] - s1 - s2) / A[i][i]

        # update value of sol
        sol = sol_new

    return sol, fail


def main():
    dim = int(input("What is the number of unknown variables? "))
    A, b = inputMatrix(dim)
    sol = np.zeros(dim)
    printMatrix("Inputted matrix", dim, A, b)
    sol, fail = gsi(dim, A, b, sol, True, 5)

    # print message
    print("Solution:" + str(sol))
    print("Error:" + str(np.dot(A, sol) - b))


if __name__ == "__main__":
    main()
