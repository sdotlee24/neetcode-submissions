# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle
        middle = head
        header = head.next
        
        while header and header.next:
            middle = middle.next
            header = header.next.next
        
        #reverse starting from middle:
        prev = None
        cur = middle
        while cur:
            nxt = cur.next       # save the next node
            cur.next = prev      # reverse the link
            prev = cur           # move prev forward
            cur = nxt            # move cur forward
        left, right = head, prev
        while left and right:
            templeft = left.next
            tempright = right.next
            left.next = right
            right.next = templeft
            right = tempright
            left = templeft
