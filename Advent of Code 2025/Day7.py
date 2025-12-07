import sys


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

    beams = set()
    start_row = 0

    for r in range(height):
        if 'S' in grid[r]:
            start_row = r
            beams.add(grid[r].index('S'))
            break

    splits = 0

    for r in range(start_row + 1, height):
        next_beams = set()
        for c in beams:
            if 0 <= c < width:
                char = grid[r][c]
                if char == '^':
                    splits += 1
                    next_beams.add(c - 1)
                    next_beams.add(c + 1)
                else:
                    next_beams.add(c)
        beams = next_beams
        if not beams:
            break

    print(splits)