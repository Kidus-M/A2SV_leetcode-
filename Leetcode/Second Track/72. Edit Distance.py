class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = [[-1] * (n + 1) for _ in range(m + 1)]

        def helper(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if memo[i][j] != -1:
                return memo[i][j]
            if word1[i] == word2[j]:
                memo[i][j] = helper(i + 1, j + 1)
            else:
                insert = 1 + helper(i, j + 1)
                delete = 1 + helper(i + 1, j)
                replace = 1 + helper(i + 1, j + 1)
                memo[i][j] = min(insert, delete, replace)
            return memo[i][j]

        return helper(0, 0)