class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        head_iters = heapq.merge(heap, *matrix)
        heap = list(head_iters)
        return heap[k-1]