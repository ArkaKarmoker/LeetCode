class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Check for empty list constraint
        if not strs:
            return ""
        
        # Sort the list of strings lexicographically
        strs.sort()
        
        # Grab the first and last strings from the sorted list
        first = strs[0]
        last = strs[-1]
        
        # Find the common prefix between the first and last string
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
            
        # Return the substring from the start up to the first mismatch
        return first[:i]
