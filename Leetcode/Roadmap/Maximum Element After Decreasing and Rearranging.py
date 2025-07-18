class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        res=0
        for i in arr:
            if i>res+1:
                res+=1
            else:
                res=i
        return res