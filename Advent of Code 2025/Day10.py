import sys
import re
import itertools


def solve_machine(line):
    # Parse target lights
    match = re.search(r'\[([.#]+)\]', line)
    if not match:
        return 0
    target_str = match.group(1)
    # Convert . to 0 and # to 1
    target = [1 if c == '#' else 0 for c in target_str]
    n_lights = len(target)

    # Parse buttons
    # Format (0,2,3)
    button_strs = re.findall(r'\(([\d,]+)\)', line)
    buttons = []
    for b_str in button_strs:
        indices = [int(x) for x in b_str.split(',')]
        vec = [0] * n_lights
        for idx in indices:
            if idx < n_lights:
                vec[idx] = 1
        buttons.append(vec)

    n_vars = len(buttons)
    if n_vars == 0:
        return 0 if sum(target) == 0 else float('inf')

    # We need to solve Ax = b over GF(2)
    # A is matrix where columns are buttons, rows are lights
    # x is vector of button presses (0 or 1)
    # b is target vector

    # Build augmented matrix [A | b]
    # Dimensions: n_lights x (n_vars + 1)
    matrix = []
    for r in range(n_lights):
        row = [buttons[c][r] for c in range(n_vars)] + [target[r]]
        matrix.append(row)

    pivot_row = 0
    pivot_cols = []
    free_vars = []

    # Gaussian Elimination (RREF)
    for col in range(n_vars):
        if pivot_row >= n_lights:
            free_vars.append(col)
            continue

        # Find pivot in current column
        pivot = -1
        for r in range(pivot_row, n_lights):
            if matrix[r][col] == 1:
                pivot = r
                break

        if pivot == -1:
            free_vars.append(col)
            continue

        # Swap rows to bring pivot to top
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        pivot_cols.append(col)

        # Eliminate other rows
        for r in range(n_lights):
            if r != pivot_row and matrix[r][col] == 1:
                for c in range(col, n_vars + 1):
                    matrix[r][c] ^= matrix[pivot_row][c]

        pivot_row += 1

    # Check for inconsistency
    # If a row is [0 0 ... 0 | 1], system is unsolvable
    for r in range(pivot_row, n_lights):
        if matrix[r][n_vars] == 1:
            return float('inf')

    # Construct Particular Solution (xp)
    # Set all free variables to 0
    xp = [0] * n_vars
    # Determine pivot variables
    # Since matrix is in RREF, for pivot row i, pivot col c:
    # 1*x_c + sum(M[i][f]*x_f) = M[i][target]
    # If free vars are 0, x_c = M[i][target]
    for i in range(len(pivot_cols)):
        c = pivot_cols[i]
        xp[c] = matrix[i][n_vars]

    # Construct Basis for Null Space
    # For each free variable f, create a basis vector where x_f=1 and others=0
    basis = []
    for f in free_vars:
        vec = [0] * n_vars
        vec[f] = 1
        # Determine pivot variables for this basis vector
        # x_c + M[i][f]*1 = 0  => x_c = M[i][f] (in GF(2))
        for i in range(len(pivot_cols)):
            c = pivot_cols[i]
            vec[c] = matrix[i][f]
        basis.append(vec)

    # Brute force search over free variables to find minimum Hamming weight
    min_presses = float('inf')

    # Iterate through all 2^k combinations of the null space basis vectors
    for coeffs in itertools.product([0, 1], repeat=len(free_vars)):
        current_solution = list(xp)

        # Add basis vectors corresponding to coeffs
        for i, coeff in enumerate(coeffs):
            if coeff:
                for j in range(n_vars):
                    current_solution[j] ^= basis[i][j]

        weight = sum(current_solution)
        if weight < min_presses:
            min_presses = weight

    return min_presses


def main():
    try:
        with open('input.txt', 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return

    total_presses = 0

    for line in lines:
        if not line.strip():
            continue

        result = solve_machine(line)

        if result == float('inf'):
            # If a machine is unsolvable, technically the total is undefined/impossible
            # But usually in these puzzles we skip or assumes valid input
            pass
        else:
            total_presses += result

    print(total_presses)


if __name__ == '__main__':
    main()