class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s=set()
        for x in nums:
            t=2
            while t*t<=x:
                while x%t==0:
                    x//=t
                    s.add(t)

                t+=1

            if x>1:
                s.add(x)

        return len(s)