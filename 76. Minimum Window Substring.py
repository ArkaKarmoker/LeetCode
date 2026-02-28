import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge cases: empty strings or s is shorter than t
        if not s or not t or len(s) < len(t):
            return ""

        # Frequency map of characters required from t
        need = collections.Counter(t)
        
        # Number of characters still needed to form a valid window
        missing = len(t)
        
        left = 0
        min_start = 0
        min_len = float('inf')

        for right, char in enumerate(s):
            # If the character is required, decrement the total missing count
            if need[char] > 0:
                missing -= 1
            
            # Decrease the needed count for the current character.
            # Characters not present in t will drop into negative values.
            need[char] -= 1

            # When the window contains all characters from t
            if missing == 0:
                # Shrink the window from the left by discarding redundant characters
                # Redundant characters are those with a negative required count
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                # Record the new minimum window if it's the smallest found so far
                current_window_len = right - left + 1
                if current_window_len < min_len:
                    min_len = current_window_len
                    min_start = left
                
                # Move the left pointer ahead by one to search for the next valid window
                need[s[left]] += 1
                missing += 1
                left += 1

        # Return the extracted substring if a valid window was found, otherwise return ""
        return "" if min_len == float('inf') else s[min_start:min_start + min_len]
