class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        g1 = [[] for _ in range(n)]
        g2 = [[] for _ in range(n)]
        for u, v, w in edges:
            g1[u].append((v, w))
            g2[v].append((u, w))

        def dijkstra(start, graph):
            dist = [float('inf')] * n
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in graph[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))
            return dist

        d1 = dijkstra(src1, g1)
        d2 = dijkstra(src2, g1)
        dr = dijkstra(dest, g2)

        ans = float('inf')
        for i in range(n):
            if d1[i] < float('inf') and d2[i] < float('inf') and dr[i] < float('inf'):
                ans = min(ans, d1[i] + d2[i] + dr[i])
        return -1 if ans == float('inf') else ans