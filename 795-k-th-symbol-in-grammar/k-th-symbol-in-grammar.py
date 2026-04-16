class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n==1:
            return 0

        length = 2 ** (n-1)
        half = length // 2


        if k <= half:
            return self.kthGrammar(n-1, k)
        else:
            return 1 - self.kthGrammar(n-1, k-half)
