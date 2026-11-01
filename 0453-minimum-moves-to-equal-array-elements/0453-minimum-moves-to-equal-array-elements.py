class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_num = min(nums)
        min_moves = 0

        for num in nums:
            min_moves += num - min_num

        return min_moves