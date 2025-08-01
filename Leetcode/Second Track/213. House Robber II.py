class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def rob_linear(arr, start, end):
            n = end - start + 1
            memo = [-1] * (n + 1)

            def helper(i):
                if i >= n:
                    return 0
                if memo[i] != -1:
                    return memo[i]
                take = arr[start + i] + helper(i + 2)
                skip = helper(i + 1)
                memo[i] = max(take, skip)
                return memo[i]

            return helper(0)

        return max(rob_linear(nums, 0, len(nums) - 2), rob_linear(nums, 1, len(nums) - 1))