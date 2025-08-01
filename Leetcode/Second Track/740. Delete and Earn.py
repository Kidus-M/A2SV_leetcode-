class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_val = max(nums)
        points = [0] * (max_val + 1)
        for num in nums:
            points[num] += num

        memo = [-1] * (max_val + 1)

        def helper(i):
            if i < 0:
                return 0
            if memo[i] != -1:
                return memo[i]
            take = points[i] + helper(i - 2)
            skip = helper(i - 1)
            memo[i] = max(take, skip)
            return memo[i]

        return helper(max_val)