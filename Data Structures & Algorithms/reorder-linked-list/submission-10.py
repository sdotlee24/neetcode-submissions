# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        inorder = res = head
        slow = fast = inorder
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        midway = slow.next
        slow.next= None
        prev = None
        # reverse
        while midway:
            temp = midway.next
            midway.next = prev
            if not temp:
                break
            prev = midway
            midway = temp
        while midway:
            postTemp = midway.next
            inTemp = inorder.next
            inorder.next = midway
            midway.next = inTemp
            inorder = inTemp
            midway = postTemp
        

