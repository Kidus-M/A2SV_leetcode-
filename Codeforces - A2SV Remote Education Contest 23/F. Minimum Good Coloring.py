n, m= map(int, input().split())
g=[[] for _ in range(n+1)]
edges=[]
for _ in range(m):
    u,v=map(int, input().split())
    edges.append((u,v))
    g[u].append(v)

visited=[0] * (n+1)
cycle=False
def dfs(u):
    global cycle
    visited[u]=1
    for v in g[u]:
        if visited[v]==0:
            dfs(v)
        elif visited[v]==1:
            cycle=True
    visited[u]=2

for i in range(1,n+1):
    if visited[i]==0:
        dfs(i)
if not cycle:
    print(1)
    print(" ".join(['1']*m))
else:
    print(2)
    colors=[]
    for u, v in edges:
        if u<v:
            colors.append("1")
        else:
            colors.append("2")
    print(" ".join(colors))