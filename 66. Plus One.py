from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Iterate through the digits from right to left
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                # Increment the current digit and return immediately
                # since there is no carry to propagate further left
                digits[i] += 1
                return digits
            
            # If the digit is 9, incrementing makes it 10. 
            # Set the current digit to 0 and let the loop handle the carry.
            digits[i] = 0
            
        # If the loop finishes without returning, all digits were 9 (e.g., 99 -> 00).
        # Prepend a 1 to account for the final carry (e.g., 00 -> 100).
        return [1] + digits
