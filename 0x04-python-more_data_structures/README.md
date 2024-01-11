This project contains a Python function named square_matrix_simple that computes the square value of all integers in a matrix.
def square_matrix_simple(matrix=[]):
Parameters:
- matrix: 2 dimensional array

Returns:
- A new matrix with each value being the square of the value of the input.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

