from sortedcontainers import SortedList
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_sorted = SortedList(nums)
        ans = []

        for n in nums:
            idx = nums_sorted.bisect_left(n)
            ans.append(idx)
            nums_sorted.remove(n)

        return ans