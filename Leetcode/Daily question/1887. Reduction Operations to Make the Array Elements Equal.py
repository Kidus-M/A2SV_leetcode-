class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        nums.sort(reverse=True)
        n = len(nums)
        for i in range(n - 1):
            if (nums[i] != nums[i + 1]):
                count += (i + 1)

        return count