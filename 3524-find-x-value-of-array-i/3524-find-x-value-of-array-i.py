class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        f = [0] * k                  
        for v in nums:
            v %= k
            g = [0] * k                 
            g[v] += 1                    
            for r in range(k):
                if f[r]:
                    g[(r * v) % k] += f[r]   
            f = g
            for r in range(k):
                result[r] += f[r]
        return result