# Jacobi Iterative
import numpy as np
ITERATION_LIMIT = 1000

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
        if np.allclose(sol, sol_new, atol=1e-10, rtol=0.):
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
