"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # two passes
        stub = Node(0)
        stub2 = res = stub
        p1 = p2 = head
        storage = {}
        while p1:
            n = Node(p1.val)
            stub.next = n
            storage[p1] = n
            stub = stub.next
            p1 = p1.next

        stub2 = stub2.next
        while p2:
            if p2.random in storage:
                stub2.random = storage[p2.random]
            stub2 = stub2.next
            p2 = p2.next
        
        return res.next

            