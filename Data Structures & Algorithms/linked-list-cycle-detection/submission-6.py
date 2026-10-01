# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        one = two = head
        two = two.next
        while two and two.next:
            if one.val == two.val:
                return True
            one = one.next
            two = two.next.next
            
        return False