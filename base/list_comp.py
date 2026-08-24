# squares = [x**2 for x in range(1,10)]

# print(squares)

# evens = [x for x in range(1,21) if x%2 == 0 ]


matrix =    [[1,2,3],
            [4,5,6],
            [7,8,9]]


# transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# print(transposed)

for i in range(len(matrix[0])):
    for row in matrix:
        print(row[i])

