class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ans=[]
        for i, v in enumerate(nums):
            if v==target:
                ans.append(i)
        return ans