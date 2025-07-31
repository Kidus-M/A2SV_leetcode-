class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def path_count(m, n):
            if (m, n) in memo:
                return memo[(m, n)]
            if m == 0 or n == 0:
                memo[(m, n)] = 0
                return 0
            elif m == 1 and n == 1:
                memo[(m, n)] = 1
                return 1
            memo[(m, n)] = path_count(m-1, n) + path_count(m, n-1)
            return memo[(m, n)]
        return path_count(m, n)