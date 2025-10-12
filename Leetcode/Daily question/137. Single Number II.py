class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_with_dup = set()

        while nums:
            num_drop = nums.pop()
            if num_drop not in nums and num_drop not in num_with_dup:
                return num_drop
            else:
                num_with_dup.add(num_drop)