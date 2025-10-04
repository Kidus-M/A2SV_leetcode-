import heapq
from collections import defaultdict
import sys
def compute_bus_dist(graph, n):
    INF = 10**18
    dist = [INF] * (n + 1)
    dist[n] = 0
    pq = [(0, n)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, l1, _ in graph[u]:
            nd = d + l1
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

def check(L, dist_bus_to_n, graph, n, t1, t2, t0):
    INF = 10**18
    dist = [INF] * (n + 1)
    dist[1] = L
    pq = [(L, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, l1, l2 in graph[u]:
            # walk
            nd = d + l2
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
            # bus
            if d + l1 <= t1 or d >= t2:
                nd = d + l1
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
    min_arr = dist[n] if dist[n] < INF else INF
    for u in range(1, n + 1):
        if dist[u] < INF and dist[u] <= t2:
            cand = t2 + dist_bus_to_n[u]
            if cand < min_arr:
                min_arr = cand
    return min_arr <= t0


input=sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    t0, t1, t2 = map(int, input().split())

    graph = defaultdict(list)
    for __ in range(m):
        u, v, l1, l2 = map(int, input().split())
        graph[u].append((v, l1, l2))
        graph[v].append((u, l1, l2))

    dist_bus_to_n = compute_bus_dist(graph, n)
    lo, hi = 0, t0
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(mid, dist_bus_to_n, graph, n, t1, t2, t0):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(ans)
