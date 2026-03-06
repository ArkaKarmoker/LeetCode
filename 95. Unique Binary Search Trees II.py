# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        # Cache to store previously computed lists of subtrees for a given range (start, end)
        memo = {}
        
        def build_trees(start: int, end: int) -> List[Optional[TreeNode]]:
            # Base case: empty range returns a list with a single None element
            if start > end:
                return [None]
            
            if (start, end) in memo:
                return memo[(start, end)]
            
            all_trees = []
            
            # Iterate through all possible root values for the current range
            for val in range(start, end + 1):
                # Recursively generate all possible left and right subtrees
                left_trees = build_trees(start, val - 1)
                right_trees = build_trees(val + 1, end)
                
                # Combine each left subtree with each right subtree using the current root
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(val)
                        root.left = l
                        root.right = r
                        all_trees.append(root)
                        
            memo[(start, end)] = all_trees
            return all_trees
        
        return build_trees(1, n)
