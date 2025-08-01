class Solution:
    def tribonacci(self, n: int) -> int:
        mem={}
        def fibb(n,mem):
            if n==0:
                return 0
            if n<=2:
                return 1
            if n not in mem:
               mem[n]=fibb(n-1,mem)+fibb(n-2,mem)+fibb(n-3,mem)
            return mem [n]
        return(fibb(n,mem))