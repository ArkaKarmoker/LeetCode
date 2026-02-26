class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Swap strings to ensure word2 is always the shorter string,
        # which minimizes the size of the 1D DP array.
        if len(word1) < len(word2):
            word1, word2 = word2, word1
            
        m, n = len(word1), len(word2)
        
        # Initialize the DP array for the base case (comparing against an empty word1)
        dp = list(range(n + 1))
        
        for i in range(1, m + 1):
            # prev_diag stores the value of dp[i-1][j-1] (the top-left diagonal)
            prev_diag = dp[0]
            
            # Update the first column for the current row (deleting all characters)
            dp[0] = i
            
            for j in range(1, n + 1):
                # Temporarily store the current dp[j] before it gets overwritten,
                # as it will become the prev_diag for the next column.
                temp = dp[j]
                
                if word1[i - 1] == word2[j - 1]:
                    # Characters match; inherit the cost from the diagonal
                    dp[j] = prev_diag
                else:
                    # Characters differ; take the minimum of the three operations
                    # dp[j - 1] : Insert
                    # dp[j]     : Delete
                    # prev_diag : Replace
                    dp[j] = 1 + min(dp[j - 1], dp[j], prev_diag)
                    
                prev_diag = temp
                
        return dp[-1]
