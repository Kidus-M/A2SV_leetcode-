class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        count = 0

        for n in nums:
            if n == 0:
                count = 0
            else:
                count += 1

            if res < count:
                res = count

        return res




