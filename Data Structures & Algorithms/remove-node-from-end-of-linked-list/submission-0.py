# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rec(head, n):
            if not head:
                return 0, None
            count, node = rec(head.next, n)
            count += 1
            if count == n:
                return count, head.next
            if count == n+1:
                head.next = node
                return count, head
            return count, head

        c, node = rec(head, n)

        return node


