print("Paste the grid lines. Empty line when done:")
rows = []
while True:
    try:
        line = input()
    except EOFError:
        break
    if line.strip() == "":
        break
    rows.append(line.rstrip("\n"))

if not rows:
    print("No input")
    raise SystemExit

h = len(rows)
w = max(len(r) for r in rows)
grid = [list(r.ljust(w, ".")) for r in rows]

dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

total_removed = 0
while True:
    to_remove = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] != "@":
                continue
            adj = 0
            for dy,dx in dirs:
                ny, nx = y+dy, x+dx
                if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == "@":
                    adj += 1
            if adj < 4:
                to_remove.append((y,x))
    if not to_remove:
        break
    for y,x in to_remove:
        grid[y][x] = "."
    total_removed += len(to_remove)

print("Total removable rolls:", total_removed)
