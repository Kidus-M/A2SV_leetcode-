import sys
import re
import itertools


def solve_machine(line):

    match = re.search(r'\[([.#]+)\]', line)
    if not match:
        return 0
    target_str = match.group(1)

    target = [1 if c == '#' else 0 for c in target_str]
    n_lights = len(target)

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
    matrix = []
    for r in range(n_lights):
        row = [buttons[c][r] for c in range(n_vars)] + [target[r]]
        matrix.append(row)

    pivot_row = 0
    pivot_cols = []
    free_vars = []


    for col in range(n_vars):
        if pivot_row >= n_lights:
            free_vars.append(col)
            continue


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

    for r in range(pivot_row, n_lights):
        if matrix[r][n_vars] == 1:
            return float('inf')
    xp = [0] * n_vars
    for i in range(len(pivot_cols)):
        c = pivot_cols[i]
        xp[c] = matrix[i][n_vars]
    basis = []
    for f in free_vars:
        vec = [0] * n_vars
        vec[f] = 1
        for i in range(len(pivot_cols)):
            c = pivot_cols[i]
            vec[c] = matrix[i][f]
        basis.append(vec)
    min_presses = float('inf')
    for coeffs in itertools.product([0, 1], repeat=len(free_vars)):
        current_solution = list(xp)
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
            pass
        else:
            total_presses += result

    print(total_presses)


if __name__ == '__main__':
    main()