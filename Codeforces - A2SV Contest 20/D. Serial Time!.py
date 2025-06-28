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
maxx = 0
directions = [(0, 0, 1), (0, 0, -1),
              (0, 1, 0), (0, -1, 0),
              (1, 0, 0), (-1, 0, 0)]


def dfs(z, i, j, time):
    global maxx
    visited[z][i][j] = True
    maxx = max(maxx, time) + 1
    for dz, dx, dy in directions:
        nz, ni, nj = dz + z, i + dx, j + dy
        if 0 <= nz < k and 0 <= ni < n and 0 <= nj < m:
            if not visited[nz][ni][nj] and grid[nz][ni][nj] == ".":
                dfs(nz, ni, nj, time + 1)


dfs(0, x, y, 0)
print(maxx)
