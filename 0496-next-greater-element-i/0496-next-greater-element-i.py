class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}

        for i in nums2:
            while stack and i > stack[-1]:
                dic[stack.pop()]=i
            stack.append(i)
        
        for i in stack:
            dic[i]=-1

        return [dic[i] for i in nums1]

