# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = ListNode()
        dummy = res = ListNode()
        while l1 or l2:
            both = carry.val
            if l1:
                both += l1.val
            if l2:
                both += l2.val
            c = both // 10
            v = both % 10
            dummy.next = ListNode(v)
            if c != 0:
                carry.val = c
            else:
                carry.val = 0
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry.val:
            dummy.next = ListNode(carry.val)
        return res.next
            