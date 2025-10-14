import sys


def is_in_square(x1, y1, half_d1, x2, y2):
    return abs(x2 - x1) <= half_d1 and abs(y2 - y1) <= half_d1


def dfs_first(graph, node, visited, finish):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_first(graph, neighbor, visited, finish)
    finish.append(node)



def dfs_second(graph, node, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_second(graph, neighbor, visited, component)

input=sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    mines = []
    for i in range(N):
        x, y, d = map(int, input().split())
        mines.append((x, y, d / 2.0, i))

    mines.sort()

    graph = [[] for _ in range(N)]
    graph_t = [[] for _ in range(N)]
    for i in range(N):
        x1, y1, half_d1, idx1 = mines[i]
        j = i + 1
        while j < N and mines[j][0] <= x1 + half_d1:
            x2, y2, half_d2, idx2 = mines[j]
            if is_in_square(x1, y1, half_d1, x2, y2):
                graph[idx1].append(idx2)
                graph_t[idx2].append(idx1)
            if is_in_square(x2, y2, half_d2, x1, y1):
                graph[idx2].append(idx1)
                graph_t[idx1].append(idx2)
            j += 1

    visited = [False] * N
    finish = []
    for i in range(N):
        if not visited[i]:
            dfs_first(graph, i, visited, finish)

    visited = [False] * N
    sccs = []
    for node in reversed(finish):
        if not visited[node]:
            component = []
            dfs_second(graph_t, node, visited, component)
            sccs.append(component)

    scc_id = [-1] * N
    for idx, component in enumerate(sccs):
        for node in component:
            scc_id[node] = idx

    indegree = [0] * len(sccs)
    for u in range(N):
        for v in graph[u]:
            if scc_id[u] != scc_id[v]:
                indegree[scc_id[v]] += 1

    print(sum(1 for deg in indegree if deg == 0))