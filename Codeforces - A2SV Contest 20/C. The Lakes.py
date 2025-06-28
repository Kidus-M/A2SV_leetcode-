def dfs(i,j):
    stack=[(i,j)]
    volume = 0
    while stack:
        x,y=stack.pop()
        if visited[x][y]:
            continue
        visited[x][y]=True
        volume += grid[x][y]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx,ny= dx + x, dy + y
            if 0<=nx <n and 0<=ny<m and grid[nx][ny]>0 and not visited[nx][ny]:
                stack.append((nx,ny))
    return volume




t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    grid=[]
    for _ in range(n):
        grid.append(list(map(int,input().split())))

    visited=[[False]*m for _ in range(n)]

    maxx=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]>0 and not visited[i][j]:
                vol =dfs(i,j)
                maxx=max(maxx,vol)

    print(maxx)
