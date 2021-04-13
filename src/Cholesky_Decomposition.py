import numpy as np
from sklearn.datasets import make_spd_matrix
from scipy.linalg import cho_factor, cho_solve
from basic_function import printMatrix


def main():
    dim = int(input("What is the number of unknown variables? "))
    # gen random A, b
    # A = symmetric positive definite
    A = make_spd_matrix(dim)
    b = np.random.rand(dim)
    printMatrix("Inputted matrix", dim, A, b)
    # c = lower tri after factorization
    c, low = cho_factor(A)
    sol = cho_solve((c, low), b)

    # print message
    print("Solution:" + str(sol))


if __name__ == "__main__":
    main()
