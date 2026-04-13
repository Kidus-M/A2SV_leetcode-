class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        idxLft, idxRgt = inf, inf
        numsLft, numsRgt = nums[:start+1][::-1], nums[start:]  

        if target in numsLft:                                   
            idxLft = numsLft.index(target)
        if target in numsRgt:
            idxRgt = numsRgt.index(target)

        return idxLft if idxLft < idxRgt else idxRgt