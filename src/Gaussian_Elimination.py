import numpy as np


# Ask users to input system of linear equation into augmented matrix of size = dim
def inputMatrix(n):
    mat = np.zeros((n, n + 1))
    for x in range(n):
        for y in range(n + 1):
            # e.g. What is M11/ M34...
            mat[x][y] = float(input("What is M" + str(x + 1) + str(y + 1) + "? "))
    return mat


# Function that prints augmented matrix
def printMatrix(message, dim, aug):
    print(message)
    for x in range(dim):
        for y in range(dim + 1):
            print("%12.4f" % aug[x][y], end=" ")
        print()


def gauEli(n, aug):
    numOfOps = 0
    ans = np.zeros(n)
    valid = True

    # To Row Echelon Form
    for pivot in range(n):
        # 1. Interchange rows if pivot = 0
        if aug[pivot][pivot] == 0:
            for x in range(pivot + 1, n):
                if aug[x][pivot] != 0:
                    # Swapping rows
                    aug[[pivot, x]] = aug[[x, pivot]]
                    numOfOps += 1
        # if rows with pivot != 0 not found -> escape
        if aug[pivot][pivot] == 0:
            valid = False
            break
        # printMatrix("Rows interchange" + str(numOfOps), dim, aug)

        # 2. Reduce the elements under the pivot to be 0
        for x in range(pivot + 1, n):
            ratio = aug[x][pivot] / aug[pivot][pivot]
            if ratio != 0:
                # Adding a multiple of top row to current row to make it 0
                for y in range(pivot, n + 1):
                    aug[x][y] -= ratio * aug[pivot][y]
                numOfOps += 1
        # printMatrix("Rows reduction" + str(numOfOps), dim, aug)
    # printMatrix("Row Reduced Form: ", dim, aug)

    if valid:
        # Normalize each row such that pivot position = 1
        for x in range(n):
            ratio = aug[x][x]
            for y in range(x, n + 1):
                aug[x][y] /= ratio
                numOfOps += 1
        # printMatrix("After normalize: ", dim, aug)

        # Back Substitution
        for x in range(n - 1, -1, -1):
            ans[x] = aug[x][n]  # store the value

            # reduce rows above
            for y in range(x):
                ratio = aug[x][n]
                aug[y][n] -= ratio * aug[y][x]
                numOfOps += 1
                aug[y][x] = 0
        # printMatrix("Reduced Row Echelon Form: ", dim, aug)

    return ans, numOfOps, valid


def main():
    dim = int(input("What is the number of unknown variables? "))
    aug = inputMatrix(dim)
    printMatrix("Inputted matrix:", dim, aug)
    sol, numOfOps, inv = gauEli(dim, aug)
    if inv:
        for i in range(dim):
            print("X" + str(i), "=", sol[i])
    else:
        print("There is no unique solution for the system.")
    print("no. of operations = " + str(numOfOps))


if __name__ == "__main__":
    main()
