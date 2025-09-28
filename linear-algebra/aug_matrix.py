# import af libraries
import numpy as np 
from sympy import Matrix, pprint

def main():

    print("=== Augumented Matrix ===\n")

    # prompting the user
    rows = int(input("Enter number of rows: m = "))
    cols = int(input("Enter number of columns: n = "))

    # asking the user to enter the elements of a matrix
    print("\n=== Enter the elementes row by row: ===\n")
    augmented_matrix = creating_matrix(rows, cols)
    print("\n===The matrix you typed is: ===\n\n", augmented_matrix)

    # Konverterer en NumPy array (matrix) til en SymPy Matrix
    matrix = Matrix(augmented_matrix)

    # Row echelon form (REF)
    ref_matrix = matrix.echelon_form()
    print("\n===REF (row echelon form)===\n")
    pprint(ref_matrix)

    # Reduced row echelon form (RREF)
    rref_matrix, pivots = matrix.rref()
    print("\n=== RREF (Reduced row echelon form) ===\n")
    pprint(rref_matrix)


    # tager alle rækker og den sidste kolonne
    solution = list(rref_matrix[:, -1])

    #lav navne: x1, x2, x3.......x100
    variables = [f"x{i+1}" for i in range(len(solution))]

    print("\n===Solution ===\n")
    #var = navnet på variablerne, zip = parrer elementerne sammen
    for var, value in zip(variables, solution):
        print(f"{var} = {float(value):.2}")


def creating_matrix(rows: int, cols: int):
    """ Generates a matrix based on user input """

    # initializing a NumPy Matrix that consists of 0's with float types.
    matrix_zeros = np.zeros((rows,cols), dtype=float)

    # replacing 0's with user-input elements
    for i in range(rows):
        for j in range(cols):
            matrix_zeros[i, j] = int(input(f"Enter element at position ({i+1},{j+1}): "))

    return matrix_zeros


if __name__ == "__main__":
    main()
