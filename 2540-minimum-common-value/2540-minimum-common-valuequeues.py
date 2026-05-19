from collections import deque
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        queue1 = deque(nums1)
        queue2 = deque(nums2)
        while queue1 and queue2:
            head1 = queue1[0]
            head2 = queue2[0]
            
            if head1 == head2:
                return head1  
            elif head1 < head2:
                queue1.popleft() 
            else:
                queue2.popleft()  
                
        return -1