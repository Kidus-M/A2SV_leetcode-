class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c=Counter(nums)
        h=[]

        for i in c:
            heapq.heappush(h,c[i])
        x=nlargest(k,h)

        ans=[]
        for i in c:
            if c[i] in x:
                ans.append(i)
        return ans