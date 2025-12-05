import sys
import bisect

def main():
    try:
        with open('input.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return

    parts = content.strip().split('\n\n')
    if len(parts) < 2:
        return

    range_lines = parts[0].splitlines()
    id_lines = parts[1].splitlines()

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

    starts = [r[0] for r in merged]
    count = 0

    for line in id_lines:
        val = int(line)
        idx = bisect.bisect_right(starts, val) - 1
        if idx >= 0:
            if val <= merged[idx][1]:
                count += 1

    print(count)

if __name__ == '__main__':
    main()