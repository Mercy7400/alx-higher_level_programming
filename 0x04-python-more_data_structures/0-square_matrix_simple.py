#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Parameters:
    - matrix: 2 dimensional array

    Returns:
    - A new matrix with each value being the square of the value of the input.
    """
    # Create a new matrix to store the squared values
    new_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row to store squared values for the current row
        new_row = []
        
        # Iterate through each element in the current row and square it
        for element in row:
            new_row.append(element ** 2)
        
        # Append the squared row to the new matrix
        new_matrix.append(new_row)

    return new_matrix

if __name__ == "__main__":
    # Test the function with the provided matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)

    # Print the result and the original matrix
    print(new_matrix)
    print(matrix)

