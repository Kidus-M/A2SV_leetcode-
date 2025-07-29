from collections import deque, defaultdict
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
a = int(data[2])
b = int(data[3])

graph = defaultdict(list)
index = 4
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    graph[u].append(v)
    graph[v].append(u)
    index += 2

visited = [False] * (n + 1)
prev = {}
queue = deque()
queue.append(a)
visited[a] = True

while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            prev[neighbor] = node
            queue.append(neighbor)

if not visited[b]:
    print(-1)
else:
    path = []
    current = b
    while current != a:
        path.append(current)
        current = prev[current]
    path.append(a)
    path.reverse()
    print(len(path) - 1)
    print(' '.join(map(str, path)))
