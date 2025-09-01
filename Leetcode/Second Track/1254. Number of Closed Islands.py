class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        id = list(range(m * n))

        def union(x: int, y: int) -> None:

            def find(x: int) -> int:
                while x != id[x]:
                    x = id[x]
                return x

            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                if root_y // n in (0, m - 1) or root_y % n in (0, n - 1):
                    id[root_x] = root_y
                else:
                    id[root_y] = root_x

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if not grid[i][j]:
                    for r, c in (i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j):
                        if not grid[r][c]:
                            union(i * n + j, r * n + c)
        return sum(not grid[i][j] and id[i * n + j] == i * n + j for i in range(1, m - 1) for j in range(1, n - 1))