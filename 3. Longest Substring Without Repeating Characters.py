class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last seen index of each character
        char_index_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            # If the character is already in the map and is inside the current window
            if current_char in char_index_map and char_index_map[current_char] >= left:
                # Move the left pointer to the right of the duplicate's last position
                left = char_index_map[current_char] + 1
            
            # Update the last seen index of the character
            char_index_map[current_char] = right
            
            # Calculate the current window size and update max_length
            max_length = max(max_length, right - left + 1)
            
        return max_length
