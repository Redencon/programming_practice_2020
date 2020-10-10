def diagonal(matrix, direction):

    """
    Calculates the sum of elements, of the main or the sub diagonal of matrix.
    Direction keywords are 'main' and 'sub'
    """

    l = len(matrix)  # length of the matrix
    s = 0  # variable for counting the sum
    if direction == 'main':
        for i in range(l):
            s += matrix[i][i]
        return s
    elif direction == 'sub':
        for i in range(l):
            s += matrix[i][l - 1 - i]
        return s
    else:
        return None


a = ((0, 1, 1), (1, 0, 1), (1, 1, 0))
print(diagonal(a, 'main'))
print(diagonal(a, 'sub'))
