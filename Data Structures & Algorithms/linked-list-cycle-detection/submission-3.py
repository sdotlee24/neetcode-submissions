# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = second = head
        second = second.next

        while first and second and second.next:
            if first.val == second.val:
                return True
            first = first.next
            second = second.next.next
        
        return False