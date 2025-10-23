# import af libraries
import numpy as np 
from sympy import Matrix, pprint
import sys

def main():


    while True:
        try:
            commands()
            choice = int(input("Choose a number: "))

            match choice:
                case 1:
                    handle_matrix_case_one()
                case 2:
                    print("under construction...🛠️")

                case 7:
                    sys.exit()

        except ValueError:
            print("Something went wrong. Enter a valid number 🙃")


def commands():
    """ Displays possible commands for the user """

    print("""\nMenu - You have the following options:\n
          1. Solve a system of linear equations (REF and RREF) using an augmented matrix
          2. Perform operations on a coefficient matrix (Transpose, Determinant, Rank)
          7. Exit the program.
          """)
    return None

def creating_matrix(rows: int, cols: int):
    """ Generates a matrix based on user input """

    # initializing a NumPy Matrix that consists of 0's with float types.
    matrix_zeros = np.zeros((rows,cols), dtype=float)

    # replacing 0's with user-input elements
    for i in range(rows):
        for j in range(cols):
            matrix_zeros[i, j] = int(input(f"Enter element at position ({i+1},{j+1}): "))

    return matrix_zeros

def handle_matrix_case_one():

    while True:
        print("\n===== Type in your augumented Matrix =====\n") 

        try:
            # prompting the user
            rows = int(input("Enter number of rows: m = "))
            cols = int(input("Enter number of columns: n = "))
        except ValueError:
            print("Invalid input. Please enter numeric values only.")
            continue

         # asking the user to enter the elements of a matrix
        print("\n=== Enter the elementes row by row: ===\n")
        augmented_matrix = creating_matrix(rows, cols)
        print("\n===The matrix you typed is: ===\n\n", augmented_matrix)

        while True:
            answer = input("\nRedo your matrix?\nType y for yes and n for no: ").lower()

            if answer == 'y':
                print("\nRedoing matrix input ...")
                break
            elif answer == 'n':
                # Konverterer en NumPy array (matrix) til en SymPy Matrix
                matrix = Matrix(augmented_matrix)

                # Row echelon form (REF)
                ref_matrix = matrix.echelon_form()
                print("\n=== REF (row echelon form) ===\n")
                pprint(ref_matrix)

                # Reduced row echelon form (RREF)
                rref_matrix, pivots = matrix.rref()
                print("\n=== RREF (Reduced row echelon form) ===\n")
                pprint(rref_matrix)


                # tager alle rækker og den sidste kolonne
                solution = list(rref_matrix[:, -1])

                #lav navne: x1, x2, x3.......x100
                variables = [f"x{i+1}" for i in range(len(solution))]

                print("\n=== Solution ===\n")
                #var = navnet på variablerne, zip = parrer elementerne sammen
                for var, value in zip(variables, solution):
                    print(f"{var} = {float(value):.2}")

                return
            
            else:
                print("Invalid choice")
                continue


if __name__ == "__main__":
    print("""
    =================================================
    This program does all the heavy thinking for you!
    Just sit back and enjoy 💅🏻
    =================================================
    """)
    main()