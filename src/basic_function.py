import numpy as np


# ask user to input augmented matrix
# return matrix A, vector b
def inputMatrix(dim):
    mat = np.zeros((dim, dim))
    vec = np.zeros(dim)
    for x in range(dim):
        for y in range(dim):
            # e.g. What is M11/ M34...
            mat[x][y] = float(input("What is M" + str(x + 1) + str(y + 1) + "? "))
        vec[x] = float(input("What is M" + str(x + 1) + str(dim + 1) + "? "))
    return mat, vec


# Function that prints augmented matrix
def printMatrix(message, dim, A, b):
    print(message)
    for x in range(dim):
        for y in range(dim):
            print("%12.4f" % A[x][y], end=" ")
        print("%12.4f" % b[x], end=" ")
        print()


# generate diagonally dominant matrix
def genddm(dim):
    A = np.random.rand(dim, dim)
    for x in range(dim):
        A[x][x] += dim
    A = (A - 0.5) * 100
    return A
