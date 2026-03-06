from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # Quick check for impossible string lengths
        if not (4 <= len(s) <= 12):
            return []
            
        result = []
        
        def backtrack(start: int, path: list):
            # Base case: 4 segments formed
            if len(path) == 4:
                # If all characters are used, a valid IP is found
                if start == len(s):
                    result.append(".".join(path))
                return
            
            # Prune paths that cannot possibly form a valid IP
            rem_chars = len(s) - start
            rem_parts = 4 - len(path)
            if rem_chars < rem_parts or rem_chars > rem_parts * 3:
                return
                
            # Try forming a segment of length 1, 2, or 3
            for length in range(1, min(4, rem_chars + 1)):
                segment = s[start:start + length]
                
                # Invalid conditions: leading zero or value > 255
                if (length > 1 and segment[0] == '0') or int(segment) > 255:
                    continue
                    
                # Add valid segment and continue DFS
                path.append(segment)
                backtrack(start + length, path)
                path.pop() # Backtrack
                
        backtrack(0, [])
        return result
