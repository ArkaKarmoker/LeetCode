class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        # Iterate through the haystack just enough times to fit the needle
        for i in range(n - m + 1):
            # Slice the haystack to the size of the needle and compare
            if haystack[i:i + m] == needle:
                return i
                
        return -1
