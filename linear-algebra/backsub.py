def back_substitution(U, b):
    """
    Løser Ux = b ved backsubstitution.
    U: øvre trekantsmatrice (liste af lister)
    b: højreside (liste)
    """
    n = len(U)
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        sum_known = sum(U[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - sum_known) / U[i][i]
    return x

# ---------------------------
# Input fra bruger
# ---------------------------

# Hvor mange ligninger / ubekendte
n = int(input("Indtast antal rækker (og ubekendte): "))

# Indlæs U
U = []
print("\nIndtast elementer til den øvre trekantsmatrice U række for række.")
for i in range(n):
    row = []
    for j in range(n):
        val = float(input(f"U[{i+1},{j+1}] = "))
        row.append(val)
    U.append(row)

# Indlæs højresiden b
b = []
print("\nIndtast højresiden b:")
for i in range(n):
    val = float(input(f"b[{i+1}] = "))
    b.append(val)

# ---------------------------
# Løs systemet
# ---------------------------
x = back_substitution(U, b)

print("\nLøsning af systemet:")
for i, xi in enumerate(x, start=1):
    print(f"x{i} = {xi}")
