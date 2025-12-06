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

    # Pad all lines to the same length to make column processing easier
    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]

    # Identify columns that are completely empty (separators)
    is_empty_col = []
    for col_idx in range(max_len):
        col_chars = [line[col_idx] for line in padded_lines]
        if all(c == ' ' for c in col_chars):
            is_empty_col.append(True)
        else:
            is_empty_col.append(False)

    # Process blocks separated by empty columns
    grand_total = 0
    current_block_start = 0

    # Add a dummy empty column at the end to ensure the last block is processed
    is_empty_col.append(True)

    for col_idx in range(len(is_empty_col)):
        if is_empty_col[col_idx]:
            # If we hit an empty column and have a pending block, process it
            if col_idx > current_block_start:
                # Extract the vertical slice for this problem
                block_lines = [line[current_block_start:col_idx] for line in padded_lines]

                numbers = []
                operator = None

                for row_str in block_lines:
                    s = row_str.strip()
                    if not s:
                        continue

                    if s in ('+', '*'):
                        operator = s
                    else:
                        # Assuming valid integer if not an operator
                        try:
                            numbers.append(int(s))
                        except ValueError:
                            pass

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