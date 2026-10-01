# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        def removeN(node):
            if not node:
                return 0
            
            count = removeN(node.next) + 1
            if count == n + 1:
                node.next = node.next.next
            return count
        
        removeN(dummy)

        return dummy.next