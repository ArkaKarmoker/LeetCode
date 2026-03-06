# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            # An empty node is valid by default
            if not node:
                return True
            
            # The current node's value must be strictly within the min and max boundaries
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively check subtrees with updated boundaries
            # Left child must be less than current node's value
            # Right child must be greater than current node's value
            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val))
        
        # Initialize with negative and positive infinity
        return validate(root, float('-inf'), float('inf'))
