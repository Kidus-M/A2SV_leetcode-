class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def helper(i):
            if i >= n - 1:
                return 0
            if memo[i] != -1:
                return memo[i]
            min_jumps = float('inf')
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    min_jumps = min(min_jumps, 1 + helper(i + j))
            memo[i] = min_jumps
            return memo[i]

        return helper(0)