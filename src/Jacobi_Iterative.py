# Jacobi Iterative
import numpy as np
from basic_function import inputMatrix, printMatrix
ITERATION_LIMIT = 1000


def jacobi(dim, A, b, sol, mes):
    fail = False
    for it_count in range(ITERATION_LIMIT):
        if it_count != 0 and mes:
            print("Iteration " + str(it_count) + ": " + str(sol))
        sol_new = np.zeros(dim)
        for i in range(dim):
            s = np.dot(A[i,:], sol)
            s = s - A[i,i] * sol[i]
            sol_new[i] = (b[i] - s) / A[i][i]

        # end if nearly same with previous sol (with tolerance)
        if np.allclose(sol, sol_new, atol=1e-8, rtol=0.):
            break

        if it_count >= ITERATION_LIMIT - 10:
            fail = True

        # update value of sol
        sol = sol_new

    return sol, fail


def main():
    dim = int(input("What is the number of unknown variables? "))
    A, b = inputMatrix(dim)
    sol = np.zeros(dim)
    printMatrix("Inputted matrix", dim, A, b)
    sol, fail = jacobi(dim, A, b, sol, True)

    # print message
    print("Solution:" + str(sol))
    print("Error:" + str(np.dot(A, sol) - b))


if __name__ == "__main__":
    main()
