class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount + 1)

        def helper(amt):
            if amt == 0:
                return 0
            if amt < 0:
                return float('inf')
            if memo[amt] != -1:
                return memo[amt]
            min_coins = float('inf')
            for coin in coins:
                min_coins = min(min_coins, 1 + helper(amt - coin))
            memo[amt] = min_coins
            return memo[amt]

        result = helper(amount)
        return result if result != float('inf') else -1