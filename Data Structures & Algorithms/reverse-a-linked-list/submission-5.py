# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 0 -> 1 -> 2 -> 3:    0 -> None, 1 -> 0 -> None
# tmp = 1, 0 -> None, prev  = 0, head = 1. tmp = 2, 1 -> 0 -> None
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead