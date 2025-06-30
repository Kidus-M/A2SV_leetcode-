k, n, m = map(int, input().split())
grid = []
for _ in range(k):
    while True:
        line=input().strip()
        if line:
            break
    layer=[]

    layer.append(list(line))
    for _ in range(n):
        line=input().strip()
        layer.append(list(line))
    grid.append(layer)
x, y = map(int, input().split())
x -= 1
y -= 1

visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(k)]
count = 0

def dfs(z, i, j):
    global count
    if not (0 <= z < k and 0 <= i < n and 0 <= j < m):
        return
    if visited[z][i][j] or grid[z][i][j] == '#':
        return

    visited[z][i][j] = True
    count += 1

    for dz, dx, dy in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        dfs(z + dz, i + dx, j + dy)

dfs(0, x, y)
print(count)
