class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        suf = [0] * n                        
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(nums[i], suf[i + 1])

        pre = float('-inf')                  
        for i in range(n):
            pre = max(pre, nums[i])
            if pre - suf[i] <= k:
                return i                     
        return -1