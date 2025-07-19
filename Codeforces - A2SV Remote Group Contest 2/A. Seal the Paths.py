import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(n)]

empty = []
start = None
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            empty.append((i, j))
            if start is None:
                start = (i, j)

parent = {}
visited = set()
q = deque()
q.append(start)
visited.add(start)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    x, y = q.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.' and (nx, ny) not in visited:
            visited.add((nx, ny))
            parent[(nx, ny)] = (x, y)
            q.append((nx, ny))

tree_nodes = list(visited)
adj = {}
for node in tree_nodes:
    adj[node] = []
for node in tree_nodes:
    if node in parent:
        p = parent[node]
        adj[p].append(node)
        adj[node].append(p)

leaves = deque()
for node in tree_nodes:
    if len(adj[node]) == 1:
        leaves.append(node)

marked = 0
while marked < k and leaves:
    node = leaves.popleft()
    x, y = node
    if grid[x][y] == '.':
        grid[x][y] = 'X'
        marked += 1
        for neighbor in adj[node]:
            adj[neighbor].remove(node)
            if len(adj[neighbor]) == 1:
                leaves.append(neighbor)

for row in grid:
    print(''.join(row))