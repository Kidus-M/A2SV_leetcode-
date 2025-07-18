class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        res=1
        for i in sorted(coins):
            if i > res:
                break
            res += i
        return res