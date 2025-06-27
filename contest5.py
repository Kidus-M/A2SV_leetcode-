import sys
input=sys.stdin.readline
n,m=map(int, input().split())
grid=[list(input().strip()) for _ in range(n)]


visited=[[False] *m for _ in range(n)]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, fx, fy,color,depth,n,m):
    if visited[x][y]:
        return False
    visited[x][y]=True
    for d in range(4):
        nx, ny=x+dx[d], y+dy[d]
        if 0<=nx<n and 0<=ny<m and grid[nx][ny]==color:
            if (nx,ny)==(fx, fy):
                continue
            if visited[nx][ny]:
                if depth>=4:
                    return True
            else:
                if dfs(nx,ny,x,y,color,depth+1,n,m):
                    return True


    return False


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if dfs(i,j,-1,-1,grid[i][j],1,n,m):
                print("Yes")
                exit()
print("No")
