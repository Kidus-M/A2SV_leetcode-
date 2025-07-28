def dfs_iterative(graph, start, visited, comp_id, labels):
    stack = [start]
    visited[start] = True
    labels[start] = comp_id
    while stack:
        v = stack.pop()
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                labels[u] = comp_id
                stack.append(u)

t = int(input())
for _ in range(t):
    n, m1, m2 = map(int, input().split())
    g_graph = [[] for _ in range(n + 1)]
    f_graph = [[] for _ in range(n + 1)]
    for _ in range(m1):
        u, v = map(int, input().split())
        f_graph[u].append(v)
        f_graph[v].append(u)
    for _ in range(m2):
        u, v = map(int, input().split())
        g_graph[u].append(v)
        g_graph[v].append(u)
    g_labels = [0] * (n + 1)
    visited = [False] * (n + 1)
    g_comp_id = 1
    for v in range(1, n + 1):
        if not visited[v]:
            dfs_iterative(g_graph, v, visited, g_comp_id, g_labels)
            g_comp_id += 1
    remove_count = 0
    filtered_f = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in f_graph[u]:
            if u < v:
                if g_labels[u] != g_labels[v]:
                    remove_count += 1
                else:
                    filtered_f[u].append(v)
                    filtered_f[v].append(u)
    f_labels = [0] * (n + 1)
    visited = [False] * (n + 1)
    f_comp_id = 1
    for v in range(1, n + 1):
        if not visited[v]:
            dfs_iterative(filtered_f, v, visited, f_comp_id, f_labels)
            f_comp_id += 1
    g_comp_to_f_comps = {}
    for v in range(1, n + 1):
        g_comp = g_labels[v]
        f_comp = f_labels[v]
        if g_comp not in g_comp_to_f_comps:
            g_comp_to_f_comps[g_comp] = set()
        g_comp_to_f_comps[g_comp].add(f_comp)
    add_count = 0
    for g_comp in g_comp_to_f_comps:
        add_count += len(g_comp_to_f_comps[g_comp]) - 1
    print(remove_count + add_count)