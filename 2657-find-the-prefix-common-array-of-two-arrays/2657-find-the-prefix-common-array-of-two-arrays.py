class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        ans=[0]*n
        seen, cnt=0, 0
        for i in range(n):
            a, b=A[i], B[i]
            seen|=1<<(2*a-1)
            cnt+= seen& 1<<(2*a)!=0
            seen|=1<<(2*b)
            cnt+= seen& 1<<(2*b-1)!=0
            ans[i]=cnt
        return ans
        
                