from collections import deque
import sys
input=sys.stdin.readline

n ,m,k=map(int,input().split())
grid=[list(input()) for _ in range(n)]

if k % 2 ==1:
    print("IMPOSSIBLE")
    exit()
startx=-1
for i in range(n):
    for j in range(m):
        if grid[i][j]=="X":
            startx=i
            start=(i,j)
            break
    if startx!=-1:
        break
dirs=["D","L","R","U"]
dx=[1,0,0,-1]
dy=[0,-1,1,0]



dist=[[-1] *m for _ in range(n)]
q=deque()
q.append(start)
dist[start[0]][start[1]]=0
while q:
    x,y=q.popleft()
    for d in range(4):
        nx, ny=x+dx[d], y+dy[d]
        if 0<=nx<n and 0<=ny<m and grid[nx][ny]!="*" and dist[nx][ny]==-1:
            dist[nx][ny]=dist[x][y] +1
            q.append((nx,ny))


adj=False
for d in range(4):
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != "*":
        adj=True
        break
if not adj:
    print("IMPOSSIBLE")
    exit()


x,y=start
ans=[]

remaining=k
while remaining >0:
    moved=False
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != "*":
            if dist[nx][ny]!= -1 and dist[nx][ny]<= remaining -1:
                ans.append(dirs[d])
                x,y=nx,ny
                remaining -=1
                moved=True
                break
    if not moved:
        print("IMPOSSIBLE")
        exit()


print("".join(ans))



