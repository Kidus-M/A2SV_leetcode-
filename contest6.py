import sys
input=sys.stdin.readline
n=int(input())
costs=list(map(int,input().split()))
to= list(map(lambda x: int(x)-1,input().split()))

visited=[0]*n
total=0

def dfs(u):
    global total
    stack=[]
    while True:
        if visited[u]==1:
            cmin=costs[u]
            v=to[u]
            while v!=u:
                cmin=min(cmin,costs[v])
                v=to[v]
            total += cmin
            break
        elif visited[u]==2:
            break
        else:
            visited[u]=1
            stack.append(u)
            u=to[u]

    for n in stack:
        visited[n]=2

for i in range(n):
    if visited[i]==0:
        dfs(i)
print(total)