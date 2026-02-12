class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] will store whether s[0...i-1] matches p[0...j-1]
        # Dimensions are (m+1) x (n+1) to handle empty strings
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base Case: Empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, a*b*c* that match empty string
        for j in range(2, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If current pattern char is '*', we have two choices:
                if p[j-1] == '*':
                    # 1. Zero occurrences: Ignore the character before '*' (move back 2 columns in p)
                    #    Example: s="c", p="ca*" -> matches "c" with "c" (ignore 'a*')
                    without_star = dp[i][j-2]
                    
                    # 2. One or more occurrences: Need current s char to match the char before '*'
                    #    If they match, we can move back 1 row in s (consume s char) but stay in same p col
                    #    Example: s="ca", p="ca*" -> matches if s="c" matches p="ca*"
                    char_match = (p[j-2] == s[i-1] or p[j-2] == '.')
                    with_star = char_match and dp[i-1][j]
                    
                    dp[i][j] = without_star or with_star
                    
                # If current pattern char is regular char or '.'
                else:
                    if p[j-1] == s[i-1] or p[j-1] == '.':
                        dp[i][j] = dp[i-1][j-1]
                        
        return dp[m][n]
