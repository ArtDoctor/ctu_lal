# Cramer's rule
import numpy as np
from common import get_number_input, get_matrix_input, determinant, get_column_input


def cramer_rule(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Solves a system of linear equations using Cramer's Rule."""
    det_A = determinant(A)

    # Check if the matrix is singular
    if det_A == 0:
        print("Warning: The matrix is singular. Cramer's Rule may not provide a unique solution.")
        return None

    solutions = []
    for i in range(len(b)):
        A_i = np.copy(A)  # Create a copy to avoid modifying the original matrix
        A_i[:, i] = b  # Replace the i-th column with the constants
        det_A_i = determinant(A_i)
        solutions.append(det_A_i / det_A)

    return np.array(solutions)


if __name__ == "__main__":
    print("Please enter the amount of rows/columns n for the (square) matrix A:")
    n = get_number_input(0, 10000000)

    print("Please enter the coefficient matrix A.")
    matrix_A = get_matrix_input(n, n)

    print("Enter the column vector of constants b:")
    b = get_column_input(n)

    solutions = cramer_rule(matrix_A, b)

    if solutions.all() is not None:
        print("The solution using Cramer's Rule is:")
        for i, x in enumerate(solutions):
            print(f"x_{i+1} = {x}")
    else:
        print("No solution could be determined.")
