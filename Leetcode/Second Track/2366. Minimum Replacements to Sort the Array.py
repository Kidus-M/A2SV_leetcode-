class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = nums[-1]
        res = 0
        for a in reversed(nums):
            k = (a + x - 1) // x
            x = a // k
            res += k - 1
        return res