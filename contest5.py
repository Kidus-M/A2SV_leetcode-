from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]

for edge_num in range(1, m + 1):
    u, v = map(int, input().split())
    graph[u].append((v, edge_num))
    indegree[v] += 1

queue = deque()

for node in range(1, n + 1):
    if indegree[node] == 0:
        queue.append(node)

last_edge = 0
ordered_nodes = 0


while queue:
    #  This mean we have multiple nodes at this point which leads to more than 1
    #  Topological ordering
    if len(queue) > 1:
        break
    u = queue.popleft()
    ordered_nodes += 1

    for v, edge_num in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
            last_edge = max(last_edge, edge_num)

if ordered_nodes != n:
    print(-1)
else:
    print(last_edge)