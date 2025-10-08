class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        for i in range(len(nums)):
            nums[i]=int(nums[i])
        nums.sort()
        return str(nums[-k])