class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * (n + 1)

        def helper(i):
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            one_step = cost[i] + helper(i + 1)
            two_step = cost[i] + helper(i + 2) if i + 2 <= n else float('inf')
            memo[i] = min(one_step, two_step)
            return memo[i]

        return min(helper(0), helper(1))