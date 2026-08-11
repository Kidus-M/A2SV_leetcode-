class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        pre_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                pre_sum += nums[i]
            else:
                break
        while pre_sum in nums:
            pre_sum += 1
        return pre_sum