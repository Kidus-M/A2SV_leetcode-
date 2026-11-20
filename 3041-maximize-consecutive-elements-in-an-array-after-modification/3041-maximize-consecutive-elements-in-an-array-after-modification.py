class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        dp0, dp1, ans = 1, 1, 1

        for lft, rgt in pairwise(nums):
            diff = rgt - lft
            if diff == 0:
                dp1 = dp0 + 1
                ans = dp1 if dp1 > ans else ans
            elif diff == 1:
                dp0+= 1
                dp1+= 1
                ans = max(ans, dp0, dp1)
            else: 
                if diff > 2:
                    dp0 = dp1 = 1
                else:
                    dp0, dp1 = dp1 + 1, 1
                    ans = dp0 if dp0 > ans else ans
            
        return ans