from collections import deque

n=int(input())
ax, ay= map(int, input().split())
bx, by =map(int, input().split())
cx, cy =map(int, input().split())


dirs=[(-1,-1),(-1,0),(-1,1), (0,-1),(0,1),(1,-1),(1,0),(1,1)]

visited=[[False] *(n+1) for _ in range(n+1)]

def isattacked(x, y, ax, ay):
    return x==ax or y ==ay or abs(x-ax)==abs(y-ay)

q=deque()
q.append((bx,by))
visited[bx][by]=True

while q:
    x, y= q.popleft()
    for dx, dy in dirs:
        nx , ny=x+dx, y+dy
        if 1 <= nx <=n and 1 <=ny <= n and not visited[nx][ny]:
            if not isattacked(nx, ny,ax,ay):
                visited[nx][ny]=True
                q.append((nx,ny))

if visited[cx][cy]:
    print("YES")
else:
    print("NO")
