# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both nodes are None, structurally identical at this leaf
        if not p and not q:
            return True
        
        # One node is None or values differ, structurally or functionally different
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively verify both left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
