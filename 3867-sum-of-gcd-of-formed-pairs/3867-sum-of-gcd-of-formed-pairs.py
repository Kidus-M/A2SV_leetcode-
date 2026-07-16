from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        gcdprefix = []
        mx = -1
        for i in nums:
            mx = max(mx, i)
            gcdprefix.append(gcd(i,mx))
        gcdprefix.sort()
        totalgcd = 0
        for i in range(len(gcdprefix)//2):
            totalgcd += gcd(gcdprefix[i], gcdprefix[-(i+1)])
        return totalgcd