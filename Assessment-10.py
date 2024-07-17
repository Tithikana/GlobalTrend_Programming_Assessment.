def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]
def original_matrix(matrix):
    for row in matrix:
        print(row)

matrix=[ [ 1,4,9],[2,7,5],[6,3,8] ]
print("Original Matrix:")
original_matrix(matrix)
transposed=transpose_matrix(matrix)
print("Transepose Matrix:")
original_matrix(transposed)
