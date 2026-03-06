# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        prev = None
        curr = root
        
        while curr:
            if not curr.left:
                # No left child, visit this node and go right
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                # Find the inorder predecessor of curr
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                
                if not pred.right:
                    # Create a temporary thread to the current node
                    pred.right = curr
                    curr = curr.left
                else:
                    # The thread already exists, meaning the left subtree is processed
                    pred.right = None  # Remove the temporary thread
                    
                    # Visit the current node
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    
                    curr = curr.right
                    
        # Swap the values of the two misplaced nodes
        if first and second:
            first.val, second.val = second.val, first.val
