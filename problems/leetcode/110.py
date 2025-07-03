from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def aux(root):
            if root is None:
                return 0

            l = aux(root.left)
            r = aux(root.right)
            if abs(l-r) > 1:
                nonlocal res            
                res = False
            
            return 1 + max(l,r)
        
        if root is None:
            return True
        

        ln = aux(root.left)
        rn = aux(root.right)
        
        if abs(ln-rn) > 1:
            return False
        return res
