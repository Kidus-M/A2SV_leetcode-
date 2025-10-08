class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]

        while pq:
            cost, i, j = heapq.heappop(pq)
            if (i, j) == (m - 1, n - 1):
                return cost
            if cost > dist[i][j]:
                continue
            for k, (dx, dy) in enumerate(dirs, 1):
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    new_cost = cost + (grid[i][j] != k)
                    if new_cost < dist[x][y]:
                        dist[x][y] = new_cost
                        heapq.heappush(pq, (new_cost, x, y))
        return dist[m - 1][n - 1]