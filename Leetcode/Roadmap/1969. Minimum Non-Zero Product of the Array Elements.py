class Solution(object):
    def minNonZeroProduct(self, p):
        """
        :type p: int
        :rtype: int
        """
        maximum=(2**p)-1
        mid=maximum//2
        mod=(10**9)+7
        res=pow(maximum-1,mid,mod)*maximum %mod
        return res