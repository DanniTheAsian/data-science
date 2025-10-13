from sympy import *
x, y, z, k, n = symbols('x y z k n')

init_printing(use_unicode=True)

def verify_base_case(formula, valid_from_n, base_case):
    """Verifies the base case for the formula at n = valid_from_n."""
    computed_base_case = (sympify(formula)).subs(n, valid_from_n)
    base_case_satisfied = computed_base_case == base_case
    return base_case_satisfied

def expand_induction_hypothesis_k_plus_1(formula, next_expression):
    """Generates the inductive hypothesis for k + 1 step."""
    inductive_step = formula.replace('n', 'k') + '+' + next_expression.replace('n', 'k')
    return expand(inductive_step)

def expand_formula_k_plus_1(formula):
    """Expands the formula for the term at n = k + 1."""
    return expand(formula.replace('n', '(k+1)'))

def prove_arithmetic_series_formula(formula, valid_from_n, base_case, next_expression):
    """Proves the formula using mathematical induction."""
    
    # Verify base case
    base_case_satisfied = verify_base_case(formula, valid_from_n, base_case)

    # Inductive step: generate the hypothesis for k + 1
    inductive_hypothesis = expand_induction_hypothesis_k_plus_1(formula, next_expression)
    formula_next_term = expand_formula_k_plus_1(formula)

    # Check if the inductive hypothesis matches the formula for the next term
    proved = base_case_satisfied and inductive_hypothesis == formula_next_term

    # Return the results
    return {
        'base_case_satisfied': base_case_satisfied,
        'inductive_hypothesis': inductive_hypothesis,
        'formula_next_term': formula_next_term,
        'proved': proved
    }

# ------ START OF SCRIPT --------

if __name__ == "__main__":
    # Input variables
    INPUT_FORMULA = 'n*(n+1)'        # Formula to prove (e.g., sum of even numbers)
    INPUT_VALID_FROM_N = 1           # Starting value for n
    INPUT_BASE_CASE = 2              # Expected base case result (sum for n=1)
    INPUT_NEXT_STEP = '2*(n+1)'      # Next step expression for induction (e.g., next even number)

    # Call the function to prove the formula
    result = prove_arithmetic_series_formula(
        INPUT_FORMULA,
        INPUT_VALID_FROM_N,
        INPUT_BASE_CASE,
        INPUT_NEXT_STEP
    )

    # Print the results
    print(result)
