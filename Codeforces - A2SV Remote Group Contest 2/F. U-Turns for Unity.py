n = int(input())

adj = {i: [] for i in range(1, n + 1)}
edges = {}

for _ in range(n):
    a, b, c = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    edges[(a, b)] = c

path = []
prev_node = -1
curr_node = 1

for _ in range(n):
    path.append(curr_node)

    if adj[curr_node][0] != prev_node:
        next_node = adj[curr_node][0]
    else:
        next_node = adj[curr_node][1]

    prev_node = curr_node
    curr_node = next_node

cost_clockwise = 0
for i in range(n):
    u = path[i]
    v = path[(i + 1) % n]
    if (v, u) in edges:
        cost_clockwise += edges[(v, u)]

cost_counter_clockwise = 0
for i in range(n):
    u = path[i]
    v = path[(i + 1) % n]
    if (u, v) in edges:
        cost_counter_clockwise += edges[(u, v)]

print(min(cost_clockwise, cost_counter_clockwise))