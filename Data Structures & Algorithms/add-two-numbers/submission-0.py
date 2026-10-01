# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 56 + 59 = 115 -> 65  95    5 1 1
        stub = p1 = ListNode()
        carry = 0
        while l1 or l2 or carry != 0:
            l1Val = l2Val = 0
            if l1:
                l1Val = l1.val
                l1 = l1.next
            if l2:
                l2Val = l2.val
                l2 = l2.next
            res = carry + l1Val + l2Val
            carry = res // 10
            rem = res % 10
            p1.next = ListNode(rem)
            p1 = p1.next
        
        return stub.next