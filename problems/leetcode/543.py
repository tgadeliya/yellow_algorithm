from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def aux(root: Optional[TreeNode]):
            if root is None:
                return 0, 0

            lmd, lmaxd = aux(root.left)         
            rmd, rmaxd = aux(root.right)
            return 1 + max(lmd, rmd), max(lmd+rmd, lmaxd, rmaxd)

        lmd, lmaxd = aux(root.left)
        rmd, rmaxd = aux(root.right)
        
        return max(lmd + rmd, lmaxd, rmaxd)

        