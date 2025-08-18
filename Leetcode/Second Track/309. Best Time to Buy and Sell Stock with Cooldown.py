class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def helper(i, state):
            if i >= n:
                return 0
            if (i, state) in memo:
                return memo[i, state]
            if state == 0:
                memo[i, state] = max(helper(i + 1, 1) - prices[i], helper(i + 1, 0))
            elif state == 1:
                memo[i, state] = max(helper(i + 1, 2) + prices[i], helper(i + 1, 1))
            else:
                memo[i, state] = helper(i + 1, 0)
            return memo[i, state]

        return helper(0, 0)