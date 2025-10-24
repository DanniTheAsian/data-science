def is_injective(mapping):
    values = list(mapping.values())
    return len(set(values)) == len(values)

def is_surjective(mapping, B):
    return set(mapping.values()) == set(B)

def is_bijective(mapping, B):
    return is_injective(mapping) and is_surjective(mapping, B)

def check_statements(A, B, mapping):
    results = {}

    # Udsagn 1: Hvis der findes en injektiv funktion f: A -> B, da er |A| <= |B|
    inj = is_injective(mapping)
    results["Hvis der findes en injektiv funktion f:A->B, da er |A|<=|B|"] = (
        not inj or len(A) <= len(B)
    )

    # Udsagn 2: Hvis der findes en surjektiv funktion f: A -> B, da er |A| >= |B|
    surj = is_surjective(mapping, B)
    results["Hvis der findes en surjektiv funktion f:A->B, da er |A|>=|B|"] = (
        not surj or len(A) >= len(B)
    )

    # Udsagn 3: Hvis der findes en bijektiv funktion f: A -> B, da er |A| = |B|
    bij = is_bijective(mapping, B)
    results["Hvis der findes en bijektiv funktion f:A->B, da er |A|=|B|"] = (
        not bij or len(A) == len(B)
    )

    for udsagn, sand in results.items():
        print(f"{udsagn}: {'SAND' if sand else 'FALSK'}")

# Eksempel
A = [1, 2, 3]
B = ['a', 'b']
f = {1: 'a', 2: 'b'}

check_statements(A, B, f)
