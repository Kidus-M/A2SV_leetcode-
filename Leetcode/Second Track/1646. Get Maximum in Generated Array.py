class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        memo = [-1] * (n + 1)
        memo[0] = 0
        memo[1] = 1

        def helper(i):
            if i > n:
                return float('-inf')
            if memo[i] != -1:
                return memo[i]
            if i % 2 == 0:
                memo[i] = helper(i // 2)
            else:
                memo[i] = helper(i // 2) + helper(i // 2 + 1)
            return memo[i]

        for i in range(n + 1):
            helper(i)
        return max(memo)