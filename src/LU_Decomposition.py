import numpy as np
import scipy.linalg as la
from basic_function import inputMatrix, printMatrix


def main():
    dim = int(input("What is the number of unknown variables? "))
    A, b = inputMatrix(dim)
    c, low = la.lu_factor(A)
    sol = la.lu_solve((c, low), b)

    printMatrix("Inputted matrix", dim, A, b)

    # print message
    print("Solution:" + str(sol))
    print("Error:" + str(np.dot(A, sol) - b))


if __name__ == "__main__":
    main()