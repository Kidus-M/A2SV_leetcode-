import heapq

n, m = map(int, input().split())

# Graph with 2 layers
adj = [[] for _ in range(2 * n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    # normal edge
    adj[u].append((v, w))
    # reversed edge in second layer
    adj[v + n].append((u + n, w))

# zero-cost transition to reversed layer
for i in range(1, n + 1):
    adj[i].append((i + n, 0))

# Dijkstra
dist = [-1] * (2 * n + 1)
pq = [(0, 1)]  # (distance, node)

while pq:
    d, u = heapq.heappop(pq)
    if dist[u] != -1:
        continue
    dist[u] = d
    for v, w in adj[u]:
        if dist[v] == -1:
            heapq.heappush(pq, (d + w, v))

# Output distances to nodes 2..n in reversed layer
print(" ".join(str(dist[i + n]) for i in range(2, n + 1)))
