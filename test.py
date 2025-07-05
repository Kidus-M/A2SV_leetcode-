import sys
input=sys.stdin.readline

n ,m,k=map(int,input().split())
grid=[list(input()) for _ in range(n)]


def isvalid(x,y):
    return 0<=x<n and 0<=y<m

def hasmoves(x,y,grid):
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    for d in range(4):
        if isvalid(x+dx,y+dy) and grid[x][y]!="*":
            return True
    return False
def canreturn(x,y,remaining,grid,startx,starty):
    return remaining>=abs(x-startx)+abs(y-starty)
dirs=["D","L","R","U"]
dx=[1,0,0,-1]
dy=[0,-1,1,0]
def dfs(x,y,steps,path,visited):
    if steps ==k :
        return path if canreturn(x,y,k-steps,grid,startx,starty) else None
    if steps >k:
        return None

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if isvalid(nx,ny) and (nx,ny) not in visited:
            newpath=path+dirs[d]
            result=dfs(nx,ny,steps+1,newpath,visited)
            if result:
                return result
            visited.remove((nx,ny))
    return None



startx=-1
for i in range(n):
    for j in range(m):
        if grid[i][j]=="X":
            startx=i
            start=(i,j)
            break
    if startx!=-1:
        break
if k % 2 ==1:
    print("IMPOSSIBLE")
    exit()
visisted={start}
startx,starty=start
ans=dfs(startx,starty,1,dirs[0],visisted)
print(ans if ans else "IMPOSSIBLE")