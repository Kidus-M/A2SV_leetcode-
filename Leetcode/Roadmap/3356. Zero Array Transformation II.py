class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        m = len(queries)
        def chk(k):
            if k == 0:
                for x in nums:
                    if x:
                        return False
                return True
            d = [0]*(n+1)
            for j in range(k):
                l, r, v = queries[j]
                d[l] += v
                if r+1 < n:
                    d[r+1] -= v
            s = 0
            for i in range(n):
                s += d[i]
                if s < nums[i]:
                    return False
            return True
        lo, hi, ans = 0, m+1, -1
        while lo < hi:
            mid = (lo+hi)//2
            if chk(mid):
                ans = mid
                hi = mid
            else:
                lo = mid+1
        return ans if ans != -1 else -1