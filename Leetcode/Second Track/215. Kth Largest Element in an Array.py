class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return nlargest(k,nums)[-1]

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minHeap = []
        for x in nums:
            heappush(minHeap, x)
            if len(minHeap) > k:
                heappop(minHeap)
        return minHeap[0]