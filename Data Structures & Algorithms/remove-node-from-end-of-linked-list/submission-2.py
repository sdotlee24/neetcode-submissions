# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rec(head, n):
            if not head:
                return None, 1
            temp, count = rec(head.next, n)
            if count != n:
                head.next = temp
                return head, count + 1
            return temp, count + 1

        node, c = rec(head, n)
        return node


