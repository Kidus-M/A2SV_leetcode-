class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def subsets(i, curr):
            if i >= len(nums):
                return curr
            return subsets(i + 1, nums[i] ^ curr) + subsets(i + 1, curr)
        return subsets(0, 0)