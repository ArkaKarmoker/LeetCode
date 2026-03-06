# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        
        while curr or stack:
            # Traverse to the leftmost node of the current subtree
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Pop the top node, record its value, and move to its right child
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
            
        return result
