from typing import List
import numpy as np


def get_number_input(min: int, max: int) -> int:
    """Gets an integer input from the user."""
    try:
        n = int(input("n: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return get_number_input(min, max)
    if n < min or n > max:
        print(f"Error: The number should be between {min} and {max}.")
        return get_number_input(min, max)
    else:
        return n


def get_column_input(n_elements: int) -> List[int]:
    """Gets a vector input from the user."""
    print("Enter the elements column/row, separated by spaces:")
    row = list(map(float, input().split()))
    if len(row) != n_elements:
        print(f"Error: The number of elements should be {n_elements}.")
        print("Please enter the row correctly.")
        return get_column_input(n_elements)
    else:
        return row


def get_matrix_input(n: int, m: int) -> np.ndarray:
    """Gets matrix input from the user.
    n: number of rows
    m: number of columns"""
    matrix = [
        get_column_input(m) for _ in range(n)
    ]
    return np.array(matrix)


def determinant(matrix: np.ndarray) -> float:
    """Calculate the determinant of a matrix."""
    # Base case: if the matrix is 1x1, return the single value.
    if matrix.size == 1:
        return matrix[0, 0]

    # Base case for 2x2 matrix:
    if matrix.shape[0] == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

    # Recursive case for NxN matrix:
    det = 0
    for column in range(matrix.shape[1]):
        # Create submatrix for minors:
        submatrix = np.delete(np.delete(matrix, 0, axis=0), column, axis=1)
        # Calculate the cofactor:
        cofactor = (-1) ** (column) * matrix[0, column] * determinant(submatrix)
        det += cofactor

    return det
