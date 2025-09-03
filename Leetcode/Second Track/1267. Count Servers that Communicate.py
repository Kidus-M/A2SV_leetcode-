class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        parent = {}
        rank = {}

        def find(x):
            if x not in parent:
                parent[x] = x
                rank[x] = 0
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for k in range(j + 1, n):
                        if grid[i][k] == 1:
                            union((i, j), (i, k))
                    for k in range(i + 1, m):
                        if grid[k][j] == 1:
                            union((i, j), (k, j))

        groups = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    root = find((i, j))
                    groups[root] = groups.get(root, 0) + 1

        return sum(count for count in groups.values() if count > 1)