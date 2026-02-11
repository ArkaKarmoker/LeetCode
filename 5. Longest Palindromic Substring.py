class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        end = 0
        
        for i in range(len(s)):
            # Case 1: Odd length palindrome (centered at i)
            len1 = self.expand_around_center(s, i, i)
            
            # Case 2: Even length palindrome (centered between i and i+1)
            len2 = self.expand_around_center(s, i, i + 1)
            
            max_len = max(len1, len2)
            
            # If we found a longer palindrome, update start and end indices
            if max_len > end - start:
                # Example: len=3, i=2. start = 2 - 1 = 1. end = 2 + 1 = 3.
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        # Return the substring (end is inclusive in logic above, so +1 for slicing)
        return s[start : end + 1]
    
    def expand_around_center(self, s: str, left: int, right: int) -> int:
        # Expand as long as indices are valid and characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return length. Note: left and right are one step beyond valid at this point.
        # Length = (right - 1) - (left + 1) + 1 = right - left - 1
        return right - left - 1
