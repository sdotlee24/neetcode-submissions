# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def sameTree(parent, child):
            if not parent and not child:
                return True
            if not parent or not child or child.val != parent.val:
                return False
            
            left, right = sameTree(parent.left, child.left), sameTree(parent.right, child.right)
            return left and right
        
        
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if sameTree(node, subRoot):
                    return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return False