class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for x in arr1:
            cnt = 0
            for y in arr2:
                if abs(x-y) > d:
                    cnt+=1
            if cnt == len(arr2):
                count+=1
        return count
