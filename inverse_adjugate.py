# calculation of an inverse matrix
# using the adjugate matrix
import numpy as np
from common import get_number_input, get_matrix_input, determinant


def calculate_minor(matrix: np.ndarray, i: int, j: int) -> float:
    """Calculate the minor of an element by removing its row and column."""
    minor_matrix = np.delete(matrix, i, axis=0)  # Delete the ith row
    minor_matrix = np.delete(minor_matrix, j, axis=1)  # Delete the jth column
    return determinant(minor_matrix)


def calculate_cofactor(matrix: np.ndarray) -> np.ndarray:
    """Calculate the cofactor matrix."""
    n = matrix.shape[0]
    cofactor_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            minor = calculate_minor(matrix, i, j)
            cofactor_matrix[i, j] = (-1)**(i + j) * minor

    return cofactor_matrix


def calculate_adjugate(matrix: np.ndarray) -> np.ndarray:
    """Calculate the adjugate by transposing the cofactor matrix."""
    cofactor_matrix = calculate_cofactor(matrix)
    adjugate_matrix = np.transpose(cofactor_matrix)
    return adjugate_matrix


def calculate_inverse(matrix: np.ndarray) -> np.ndarray:
    """Calculate the inverse of the matrix using the adjugate method."""
    det = determinant(matrix)
    if np.isclose(det, 0):
        return None  # The matrix is singular, so it does not have an inverse.

    adjugate_matrix = calculate_adjugate(matrix)
    inverse_matrix = adjugate_matrix / det
    return inverse_matrix


if __name__ == "__main__":
    print("Please enter the amount of rows/columns n for the (square) matrix A:")
    n = get_number_input(0, 10000000)

    print("Please enter the matrix A:")
    matrix = get_matrix_input(n, n)

    inverse_matrix = calculate_inverse(matrix)

    if inverse_matrix is None:
        print("The input matrix is singular and does not have an inverse.")
    else:
        print("Inverse Matrix:")
        print(inverse_matrix)

        print('#' * 50)
        print("Dot product (for testing purposes; should look like identity matrix): \n",
              np.dot(matrix, inverse_matrix))
