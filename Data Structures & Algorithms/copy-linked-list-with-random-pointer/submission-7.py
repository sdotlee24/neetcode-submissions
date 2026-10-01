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
        nodeMap = {}
        curr = head
        
        while curr:
            nodeMap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            copy = nodeMap[curr]

            copy.next = nodeMap.get(curr.next)
            copy.random = nodeMap.get(curr.random)

            curr = curr.next
        
        return nodeMap.get(head)