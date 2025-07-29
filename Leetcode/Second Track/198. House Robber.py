class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def go(pos):
            if pos >= n:
                return 0

            if pos in memo:
                return memo[pos]

            memo[pos] = max(
                go(pos+1),
                nums[pos] + go(pos+2)
            )
            return memo[pos]


        return go(0)