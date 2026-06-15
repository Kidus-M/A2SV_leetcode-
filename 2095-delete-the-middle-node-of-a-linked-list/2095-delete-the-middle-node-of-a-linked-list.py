# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        container = deque()
        curr = head
        while curr:
            container.append(curr)
            curr = curr.next
            
        total = len(container)
        mid = total // 2
        prev_node = container[mid - 1]
        node_to_remove = container[mid]
        
        prev_node.next = node_to_remove.next
            
        return head