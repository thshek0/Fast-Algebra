# improved version of Jacobi Iterative
# condition: converge system, i.e. diagonally dominant
# not suitable for all systems, e.g. [1,2,3][4,5,6]
import numpy as np
ITERATION_LIMIT = 1000


def inputMatrix():
    mat = np.zeros((dim, dim))
    vec = np.zeros(dim)
    for x in range(dim):
        for y in range(dim):
            # e.g. What is M11/ M34...
            mat[x][y] = float(input("What is M" + str(x + 1) + str(y + 1) + "? "))
        vec[x] = float(input("What is M" + str(x + 1) + str(dim + 1) + "? "))
    return mat, vec


# Function that prints augmented matrix
def printMatrix(message):
    print(message)
    for x in range(dim):
        for y in range(dim):
            print("%12.4f" % A[x][y], end=" ")
        print("%12.4f" % b[x], end=" ")
        print()


dim = int(input("What is the number of unknown variables? "))
A, b = inputMatrix()
sol = np.zeros(dim)
printMatrix("Inputted matrix")

for it_count in range(ITERATION_LIMIT):
    if it_count != 0:
        print("Iteration {0}: {1}".format(it_count, sol))
    sol_new = np.zeros(dim)

    for i in range(dim):
        s1 = np.dot(A[i, :i], sol_new[:i])
        s2 = np.dot(A[i, i + 1:], sol[i + 1:])
        sol_new[i] = (b[i] - s1 - s2) / A[i][i]
        # if sol_new[i] == sol_new[i-1]:
        #    break

    # end if nearly same with previous sol (with tolerance)
    if np.allclose(sol, sol_new, atol=1e-10, rtol=0.):
        break

    # update value of sol
    sol = sol_new

# print message
print("Solution:" + str(sol))
print("Error:" + str(np.dot(A, sol) - b))
