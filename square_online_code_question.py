def find_neighbours(A, B, val, x, y, ):
    if x < 0 or x > len(A) - 1:
        return
    if y < 0 or y > len(A[0]) - 1:
        return
    if B[x][y] == False:
        return
    if A[x][y] != val:
        return

    B[x][y] = False

    find_neighbours(A, B, val, x+1, y)
    find_neighbours(A, B, val, x-1, y)
    find_neighbours(A, B, val, x, y+1)
    find_neighbours(A, B, val, x, y-1)


def calculateNumberOfCountries(A):

    sum = 0
    B = [[True for x in A[0]] for y in A]

    for x in range(0, len(A)):
        for y in range(0, len(A[x])):
            if B[x][y] == False:
                continue
            sum += 1
            find_neighbours(A, B, A[x][y], x, y)
    return sum


if __name__ == "__main__":
    A = [[5, 4, 4], [4, 3, 4], [3, 2, 4], [2, 2, 2], [3, 3, 4], [1, 4, 4], [4, 1, 1]]
    print(calculateNumberOfCountries(A))