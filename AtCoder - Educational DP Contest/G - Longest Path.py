from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
indeg = [0] * N

for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)
    indeg[y] += 1


q = deque([i for i in range(N) if indeg[i] == 0])
topo = []
while q:
    u = q.popleft()
    topo.append(u)
    for v in graph[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)


dp = [0] * N
for u in topo:
    for v in graph[u]:
        dp[v] = max(dp[v], dp[u] + 1)

print(max(dp))