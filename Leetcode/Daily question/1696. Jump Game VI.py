class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap=[(0,-k)]
        for i in range(len(nums)):
            while i-heap[0][1]>k: heappop(heap)
            nums[i]-=heap[0][0]
            heappush(heap,(-nums[i],i))
        return nums[-1]