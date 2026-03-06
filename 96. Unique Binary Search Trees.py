class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] represents the number of unique BSTs that can be formed with i nodes
        dp = [0] * (n + 1)
        
        # Base cases: an empty tree (0 nodes) or a tree with 1 node exactly 1 combination
        dp[0] = 1
        dp[1] = 1
        
        # Build the solutions for tree sizes from 2 up to n
        for i in range(2, n + 1):
            # Try making every number from 1 to i the root of the tree
            for j in range(1, i + 1):
                # Multiply the combinations of the left subtree by the right subtree
                # Left subtree gets j - 1 nodes, right subtree gets i - j nodes
                dp[i] += dp[j - 1] * dp[i - j]
                
        return dp[n]
