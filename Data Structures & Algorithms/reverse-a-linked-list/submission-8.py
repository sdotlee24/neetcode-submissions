# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        temp = head
        prev = None
        # 0 -> 1 | <- 0
        while temp:
            placeholder = temp.next
            temp.next = prev
            prev = temp
            if not placeholder:
                return temp
            temp = placeholder
            