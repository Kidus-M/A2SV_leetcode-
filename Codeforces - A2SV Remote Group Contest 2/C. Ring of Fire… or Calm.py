n, m = map(int, input().split())
chords = []

for _ in range(m):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    chords.append((a, b))

adj = [[] for _ in range(m)]

for i in range(m):
    a1, b1 = chords[i]
    for j in range(i + 1, m):
        a2, b2 = chords[j]
        if (a1 < a2 < b1 < b2) or (a2 < a1 < b2 < b1):
            adj[i].append(j)
            adj[j].append(i)

color = [-1] * m

from collections import deque
for i in range(m):
    if color[i] == -1:
        queue = deque()
        queue.append(i)
        color[i] = 0
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    print("Impossible")
                    exit()

res = []
for c in color:
    res.append('i' if c == 0 else 'o')
print(''.join(res))
