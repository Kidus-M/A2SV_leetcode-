class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n+1000):
            x=i
            pr=1
            while x>0:
                pr*=x%10
                x//=10
            if pr%t==0:
                return i
                
        