class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        dist = [[INF]*n for _ in range(m)]
        dist[0][0] = grid[0][0]
        pq = [(grid[0][0], 0, 0)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while pq:
            d, x, y = heapq.heappop(pq)
            if d > dist[x][y]:
                continue
            if x == m - 1 and y == n - 1:
                return d < health
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nd = d + grid[nx][ny]
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        heapq.heappush(pq, (nd, nx, ny))
        return False