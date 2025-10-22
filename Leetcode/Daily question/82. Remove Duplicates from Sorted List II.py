# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        neww = ListNode(0, head)
        head = neww

        temp = head.next
        prev = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                while temp.next and temp.val == temp.next.val:
                    temp = temp.next
                prev.next = temp.next
            else:
                prev = prev.next
            temp = temp.next

        return head.next