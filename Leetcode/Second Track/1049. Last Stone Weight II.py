class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for stone in stones:
            next_dp = dp[:]
            for i in range(stone, target + 1):
                if dp[i - stone]:
                    next_dp[i] = True
            dp = next_dp

        for i in range(target, -1, -1):
            if dp[i]:
                return total - 2 * i
        return 0