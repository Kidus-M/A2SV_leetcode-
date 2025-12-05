import sys


def main():
    try:
        with open('input.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return

    parts = content.strip().split('\n\n')

    range_lines = parts[0].splitlines()

    ranges = []
    for line in range_lines:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))

    ranges.sort()

    merged = []
    if ranges:
        curr_start, curr_end = ranges[0]
        for next_start, next_end in ranges[1:]:
            if next_start <= curr_end + 1:
                curr_end = max(curr_end, next_end)
            else:
                merged.append((curr_start, curr_end))
                curr_start, curr_end = next_start, next_end
        merged.append((curr_start, curr_end))

    total_fresh = 0
    for start, end in merged:
        total_fresh += (end - start + 1)

    print(total_fresh)


if __name__ == '__main__':
    main()