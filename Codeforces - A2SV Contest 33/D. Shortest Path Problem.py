n, m = map(int, input().split())
graph=[[] for i in range(n+1)]
edges=[]
for _ in range(m):
    a,b,w = map(int, input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))
    edges.append((a,b,w))

from collections import deque
dist=[-1]*(n+1)
dist[1]=0

q=deque([1])


while q:
    u=q.popleft()
    for v, w in graph[u]:
        if dist[v]==-1:
            dist[v]=dist[u]^w
            q.append(v)

basis=[]
for a,b,w in edges:
    val = dist[a] ^ dist[b] ^ w
    if val ==0:
        continue
    for b in basis:
        val = min(val, val ^ b)
    if val:
        basis.append(val)
        basis.sort(reverse=True)


ans=dist[n]
for b in basis:
    ans=min(ans^b,ans)
print(ans)