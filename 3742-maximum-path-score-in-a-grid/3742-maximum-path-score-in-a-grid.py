class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        @cache
        def solve(i, j, p):
            if i>=len(grid) or j>=len(grid[0]): return -float("inf")
            p -= min(grid[i][j], 1)
            if p<0: return -float("inf")
            if (i, j) == (len(grid)-1, len(grid[0])-1): return grid[i][j]
            return grid[i][j] + max(solve(i+1, j, p), solve(i, j+1, p))
        ans = solve(0, 0, k)
        solve.cache_clear()
        return -1 if ans == -float("inf") else ans