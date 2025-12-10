import sys
import re
import itertools
from fractions import Fraction


def solve_machine(line):
    match = re.search(r'\{([\d,]+)\}', line)
    if not match:
        return 0
    target_str = match.group(1)
    target = [int(x) for x in target_str.split(',')]
    n_counters = len(target)

    button_strs = re.findall(r'\(([\d,]+)\)', line)
    buttons = []
    for b_str in button_strs:
        indices = [int(x) for x in b_str.split(',')]
        vec = [0] * n_counters
        for idx in indices:
            if idx < n_counters:
                vec[idx] = 1
        buttons.append(vec)

    n_vars = len(buttons)
    if n_vars == 0:
        return 0 if sum(target) == 0 else float('inf')
    matrix = []
    for r in range(n_counters):
        row = [Fraction(buttons[c][r]) for c in range(n_vars)] + [Fraction(target[r])]
        matrix.append(row)

    pivot_row = 0
    pivot_cols = []
    free_vars = []

    for col in range(n_vars):
        if pivot_row >= n_counters:
            free_vars.append(col)
            continue

        pivot = -1
        for r in range(pivot_row, n_counters):
            if matrix[r][col] != 0:
                pivot = r
                break

        if pivot == -1:
            free_vars.append(col)
            continue

        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        pivot_cols.append(col)
        divisor = matrix[pivot_row][col]
        for c in range(col, n_vars + 1):
            matrix[pivot_row][c] /= divisor

        for r in range(n_counters):
            if r != pivot_row and matrix[r][col] != 0:
                factor = matrix[r][col]
                for c in range(col, n_vars + 1):
                    matrix[r][c] -= factor * matrix[pivot_row][c]

        pivot_row += 1
    for r in range(pivot_row, n_counters):
        if matrix[r][n_vars] != 0:
            return float('inf')

    bounds = []
    for j in range(n_vars):
        upper = float('inf')
        col_vec = buttons[j]
        has_effect = False
        for r in range(n_counters):
            if col_vec[r] > 0:
                has_effect = True
                upper = min(upper, target[r])
        bounds.append(upper if has_effect else 0)


    min_total = float('inf')
    ranges = [range(bounds[f] + 1) for f in free_vars]
    for free_vals in itertools.product(*ranges):
        valid = True
        current_x = [0] * n_vars
        for i, f_col in enumerate(free_vars):
            current_x[f_col] = free_vals[i]
        for i, p_col in enumerate(pivot_cols):
            val = matrix[i][n_vars]
            for idx, f_col in enumerate(free_vars):
                val -= matrix[i][f_col] * free_vals[idx]
            if val.denominator != 1 or val < 0:
                valid = False
                break
            current_x[p_col] = int(val)

        if valid:
            total = sum(current_x)
            if total < min_total:
                min_total = total

    return min_total


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