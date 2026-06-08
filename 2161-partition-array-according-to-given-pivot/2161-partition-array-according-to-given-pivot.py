class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        leftArr=[]
        rightArr=[]
        pivCnt=0
        for i in range(0, n):
            if nums[i]==pivot:
                pivCnt+=1
            elif nums[i]>pivot:
                rightArr.append(nums[i])                
            else:
                leftArr.append(nums[i])                
        
        return leftArr+[pivot]*pivCnt+rightArr