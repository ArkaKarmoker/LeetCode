class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx, p_idx = 0, 0
        star_idx = -1
        match_idx = 0
        
        while s_idx < len(s):
            # Characters match, or pattern has '?', so move both pointers forward
            if p_idx < len(p) and (p[p_idx] == '?' or s[s_idx] == p[p_idx]):
                s_idx += 1
                p_idx += 1
                
            # Found a '*', record its position and assume it matches the empty string for now
            elif p_idx < len(p) and p[p_idx] == '*':
                star_idx = p_idx
                match_idx = s_idx
                p_idx += 1
                
            # Mismatch occurred, but we have a previous '*' to fall back on
            elif star_idx != -1:
                # Let the '*' match one more character from 's' and try again
                p_idx = star_idx + 1
                match_idx += 1
                s_idx = match_idx
                
            # Mismatch, and no '*' to save us
            else:
                return False
                
        # Check if there are remaining characters in pattern (they must all be '*')
        while p_idx < len(p) and p[p_idx] == '*':
            p_idx += 1
            
        return p_idx == len(p)
