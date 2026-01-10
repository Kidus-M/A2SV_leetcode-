import heapq

n, m = map(int, input().split())

adj = [[] for _ in range(2 * n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v + n].append((u + n, w))
for i in range(1, n + 1):
    adj[i].append((i + n, 0))

dist = [-1] * (2 * n + 1)
pq = [(0, 1)]

while pq:
    d, u = heapq.heappop(pq)
    if dist[u] != -1:
        continue
    dist[u] = d
    for v, w in adj[u]:
        if dist[v] == -1:
            heapq.heappush(pq, (d + w, v))
print(" ".join(str(dist[i + n]) for i in range(2, n + 1)))
