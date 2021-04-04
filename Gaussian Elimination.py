import numpy as np
from numpy import random


# Function that prints augmented matrix
def printMatrix():
    # print("The matrix:")
    for x in range(dim):
        for y in range(dim + 1):
            print("%12.4f" % aug[x][y], end=" ")
        print()


dim = int(input("What is the number of unknown variables? "))
numOfOps = 0
ratio = 1
ans = np.zeros(dim)
# aug = np.zeros((dim, dim+1))
valid = True
'''
# Ask for input of augmented matrix (system)
for i in range(dim):
    for j in range(dim+1):
        # e.g. What is M11/ M34...
        aug[i][j] = float(input("What is M" + str(i+1) + str(j+1) + "? "))
'''
# if u need random test case...
aug = random.rand(dim, dim+1)
print("Inputted Matrix: ")
printMatrix()

# To Row Echelon Form
for pivot in range(dim):
    # 1. Interchange rows if pivot = 0
    if aug[pivot][pivot] == 0:
        for i in range(pivot+1, dim):
            if aug[i][pivot] != 0:
                # Swapping rows
                aug[[pivot, i]] = aug[[i, pivot]]
                numOfOps += 1
    # if rows with pivot != 0 not found -> escape
    if aug[pivot][pivot] == 0:
        valid = False
        break
    # print("Rows interchange" + str(numOfOps))
    # printMatrix()

    # 2. Reduce the elements under the pivot to be 0
    for i in range(pivot+1, dim):
        ratio = aug[i][pivot] / aug[pivot][pivot]
        if ratio != 0:
            # Adding a multiple of top row to current row to make it 0
            for j in range(pivot, dim+1):
                aug[i][j] -= ratio * aug[pivot][j]
            numOfOps += 1
    # print("Rows reduction" + str(numOfOps))
    # printMatrix()
print("Row Reduced Form: ")
printMatrix()

if valid:
    # Normalize each row such that pivot position = 1
    for i in range(dim):
        ratio = aug[i][i]
        for j in range(i, dim+1):
            aug[i][j] /= ratio
            numOfOps += 1
    # printMatrix()

    # Back Substitution
    for i in range(dim-1, -1, -1):
        ans[i] = aug[i][dim]  # store the value

        # reduce rows above
        for j in range(i):
            ratio = aug[i][dim]
            aug[j][dim] -= ratio * aug[j][i]
            numOfOps += 1
            aug[j][i] = 0
    print("Reduced Row Echelon Form: ")
    printMatrix()

    for i in range(dim):
        print("X" + str(i), "=", ans[i])
else:
    print("There is no unique solution for the system.")

print("no. of operations = " + str(numOfOps))
