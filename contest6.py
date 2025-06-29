import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    # Tarjan's bridge-finding (ITERATIVE)
    timer = [0]
    tin = [-1] * n
    low = [-1] * n
    bridges = []

    stack = []
    parent = [-1] * n
    visited = [False] * n

    for start in range(n):
        if tin[start] != -1:
            continue
        stack.append((start, 0, None))  # (node, child index, parent)
        while stack:
            v, idx, p = stack[-1]
            if tin[v] == -1:
                tin[v] = low[v] = timer[0]
                timer[0] += 1
                parent[v] = p
            neighbors = graph[v]
            if idx < len(neighbors):
                to = neighbors[idx]
                stack[-1] = (v, idx + 1, p)
                if to == p:
                    continue
                if tin[to] != -1:
                    low[v] = min(low[v], tin[to])
                else:
                    stack.append((to, 0, v))
            else:
                stack.pop()
                if p is not None:
                    low[p] = min(low[p], low[v])
                    if low[v] > tin[p]:
                        bridges.append((p, v))

    total_pairs = n * (n - 1) // 2
    min_reachable = total_pairs

    # For each bridge, compute component sizes (ITERATIVE DFS)
    def component_size(start, skip_u, skip_v):
        stack = [start]
        visited = [False] * n
        visited[start] = True
        count = 1
        while stack:
            node = stack.pop()
            for nei in graph[node]:
                if visited[nei]:
                    continue
                if (node == skip_u and nei == skip_v) or (node == skip_v and nei == skip_u):
                    continue
                visited[nei] = True
                stack.append(nei)
                count += 1
        return count

    for u, v in bridges:
        sz = component_size(u, u, v)
        other = n - sz
        reachable = sz * (sz - 1) // 2 + other * (other - 1) // 2
        min_reachable = min(min_reachable, reachable)

    print(min_reachable)
