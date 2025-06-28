import sys
input=sys.stdin.readline

t = int(input())


def dfs(node, visited, graph):
    visited[node] = True
    count = 1
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(neighbor, visited, graph)
    return count


for _ in range(t):
    n, m = map(int, input().split())
    edges = []
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)

    total = n * (n - 1) // 2
    minn = float('inf')

    for u, v in edges:
        graph[u].remove(v)
        graph[v].remove(u)
        visited = [False] * (n + 1)
        size = dfs(u, visited, graph)
        other = n - size
        unreachable = size * other
        reachable = total - unreachable
        minn = min(minn, reachable)
        graph[u].append(v)
        graph[v].append(u)

    print(minn)
