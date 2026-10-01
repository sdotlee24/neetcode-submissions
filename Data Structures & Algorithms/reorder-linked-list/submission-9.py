class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Split into two lists
        second = slow.next
        slow.next = None
        # Reverse second half
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        second = prev

        # Merge
        first = head

        while first and second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2