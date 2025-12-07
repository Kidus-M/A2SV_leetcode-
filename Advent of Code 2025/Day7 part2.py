import sys
from collections import defaultdict


def main():
    try:
        with open('input.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return

    grid = content.strip().splitlines()
    if not grid:
        return

    height = len(grid)
    width = len(grid[0])
    beams = defaultdict(int)
    start_row = 0

    for r in range(height):
        if 'S' in grid[r]:
            start_row = r
            beams[grid[r].index('S')] = 1
            break

    total_timelines = 0

    for r in range(start_row + 1, height):
        next_beams = defaultdict(int)

        for c, count in beams.items():
            if not (0 <= c < width):
                total_timelines += count
                continue

            char = grid[r][c]
            if char == '^':
                next_beams[c - 1] += count
                next_beams[c + 1] += count
            else:

                next_beams[c] += count

        beams = next_beams
        if not beams:
            break

    for c, count in beams.items():
        total_timelines += count

    print(total_timelines)


if __name__ == '__main__':
    main()