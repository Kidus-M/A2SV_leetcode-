import sys


def main():
    try:
        with open('input.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return

    lines = content.splitlines()
    if not lines:
        return

    # Pad all lines to the same length
    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]

    # Identify empty columns (separators)
    is_empty_col = []
    for col_idx in range(max_len):
        col_chars = [line[col_idx] for line in padded_lines]
        if all(c == ' ' for c in col_chars):
            is_empty_col.append(True)
        else:
            is_empty_col.append(False)

    grand_total = 0
    current_block_start = 0

    # Add a dummy empty column at the end to ensure the last block is processed
    is_empty_col.append(True)

    # The last row contains the operators
    operator_row_idx = len(padded_lines) - 1

    for col_idx in range(len(is_empty_col)):
        if is_empty_col[col_idx]:
            # Process the block if it exists
            if col_idx > current_block_start:
                # Find the operator in this block's slice of the last row
                op_slice = padded_lines[operator_row_idx][current_block_start:col_idx]
                operator = op_slice.strip()

                # If we found multiple chars, it might be an issue, but usually it's just one op per block
                # We'll assume the first valid char is the operator
                if len(operator) > 1:
                    operator = operator[0]  # Just in case

                numbers = []

                # Iterate columns in this block from RIGHT to LEFT
                for c in range(col_idx - 1, current_block_start - 1, -1):
                    # Construct number from this column (all rows except the last one)
                    digit_chars = []
                    for r in range(len(padded_lines) - 1):
                        char = padded_lines[r][c]
                        if char.isdigit():
                            digit_chars.append(char)

                    if digit_chars:
                        number_str = "".join(digit_chars)
                        numbers.append(int(number_str))

                # Calculate result for this problem
                if numbers and operator:
                    result = numbers[0]
                    for num in numbers[1:]:
                        if operator == '+':
                            result += num
                        elif operator == '*':
                            result *= num
                    grand_total += result

            # Reset start for the next potential block
            current_block_start = col_idx + 1

    print(grand_total)


if __name__ == '__main__':
    main()