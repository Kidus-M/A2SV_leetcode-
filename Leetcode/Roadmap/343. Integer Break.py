class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        for k in range(2, n):
            x = n // k
            b = n % k
            a = k - b
            res = max(res, pow(x, a) * pow(x + 1, b))
        return res