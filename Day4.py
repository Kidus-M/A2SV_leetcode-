print("Paste grid, empty line = done:")
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
count = 0
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
            count += 1

print("Accessible rolls:", count)
