class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        
        # Base check: total lengths must match
        if m + n != len(s3):
            return False
            
        # dp[j] represents whether s3[:i+j] can be formed by interleaving s1[:i] and s2[:j]
        dp = [False] * (n + 1)
        
        # Both strings are empty
        dp[0] = True
        
        # Initialize the first row (using 0 characters from s1)
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            
        # Process the remaining rows
        for i in range(1, m + 1):
            # Update the first element of the current row (using 0 characters from s2)
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            
            for j in range(1, n + 1):
                # Two possibilities to form a valid interleave up to the current characters:
                # 1. The previous character in s3 matched s1, and the current state was valid (dp[j])
                # 2. The previous character in s3 matched s2, and the previous state was valid (dp[j-1])
                match_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]
                match_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                
                dp[j] = match_s1 or match_s2
                
        return dp[n]
