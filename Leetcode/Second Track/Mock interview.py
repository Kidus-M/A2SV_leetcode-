"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
You may change 0's to 1's to connect the two islands to form one island.
Return the smallest number of 0's you must flip to connect the two islands.


Example 1:
Input: grid = [[0,1],[1,0]]
Output: 1


Example 2:
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2


Example 3:
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


Constraints:


n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.

[0,1,0]
[0,0,0]
[0,0,1]



"""
from collections import deque

grid = [[0,1],[1,0]]
n = len(grid)
visited = [[False] * n for _ in range(n)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y, q):
    if x < 0 or x >= n or y < 0 or y >= n or grid[x][y]==0 or visited[x][y]:
        return
    visited[x][y] = True
    q.append((x, y))
    for dx, dy in directions:
        dfs(x + dx, y + dy, q)

q = deque()
found = False

for i in range(n):
    if found: break
    for j in range(n):
        if grid[i][j] == 1:
            dfs(i, j, q)
            found = True
            break

ans = 0
while q:
    for _ in range(len(q)):
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0<=nx<n and  0<=ny<n and not visited[nx][ny]:
                if grid[nx][ny] == 1:
                    print(ans)
                visited[nx][ny] = True
                q.append((nx, ny))
    ans += 1
