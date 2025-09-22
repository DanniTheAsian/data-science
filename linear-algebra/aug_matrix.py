# import af libraries
import numpy as np 
from sympy import Matrix


#En numpy array med flere lister
Augmented_Matrix = np.array([
    [1,1,0,3], #R1 x1 + x2
    [0,1,-1,2], #R2 x2 + x3
    [2,1,1,4] #R3 x1 + x2 + x3
    #tilføj flere lister, hvis nødvendigt
])
#Konverter matrix 
matrix = Matrix(Augmented_Matrix)

#Row echelon form
ref_matrix = matrix.echelon_form()
print("===REF (row echelon form)===")
print (ref_matrix)

#Reduced echelon form
rref_matrix, pivots = matrix.rref()
print("\n=== RREF (Reduced row echelon form)===")
print(rref_matrix)

#tager alle rækker og den sidste kolonne
solution = list(rref_matrix[:, -1])

#lav navne: x1, x2, x3.......x100
variables = [f"x{i+1}" for i in range(len(solution))]

print("\n===Solution ===")
#var = navnet på variablerne, zip = parrer elementerne sammen
for var, value in zip(variables, solution):
    print(f"{var} = {float(value):.2}")