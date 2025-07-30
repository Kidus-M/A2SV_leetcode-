import sys
import heapq
from collections import defaultdict, deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    # Full DAG: u < v
    graph = defaultdict(list)
    indegree = [0] * (N + 1)

    # Mark removed edges
    removed = set()
    for _ in range(M):
        a, b = map(int, input().split())
        removed.add((a, b))

    # Rebuild graph excluding removed edges
    for u in range(1, N + 1):
        for v in range(u + 1, N + 1):
            if (u, v) not in removed:
                graph[u].append(v)
                indegree[v] += 1

    # Use max-heap for lexicographically largest sort
    heap = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(heap, -i)  # max-heap by negating

    result = []
    while heap:
        u = -heapq.heappop(heap)
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heapq.heappush(heap, -v)

    print(' '.join(map(str, result)))
