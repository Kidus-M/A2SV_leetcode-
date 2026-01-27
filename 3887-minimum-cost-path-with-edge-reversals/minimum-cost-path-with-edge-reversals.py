class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))

        pq = [(0, 0)]
        min_costs = [float('inf')] * n
        min_costs[0] = 0

        while pq:
            d, u = heapq.heappop(pq)
            if u == n - 1:
                return d
            if d > min_costs[u]:
                continue

            for v, w in adj[u]:
                new_cost = d + w
                if new_cost < min_costs[v]:
                    min_costs[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

        return -1