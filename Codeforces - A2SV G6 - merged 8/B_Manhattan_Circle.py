t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(input().strip())

    hashes = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                hashes.append((i + 1, j + 1))
    rows = [pos[0] for pos in hashes]
    cols = [pos[1] for pos in hashes]

    center_row = (min(rows) + max(rows)) // 2
    center_col = (min(cols) + max(cols)) // 2

    print(center_row, center_col)