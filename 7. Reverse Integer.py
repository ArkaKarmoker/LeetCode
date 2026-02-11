class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer range
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        
        # Handle the sign and work with absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_x = 0
        
        # Reverse the digits mathematically
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for potential overflow before updating reversed_x
            # (Though Python handles large ints, this logic respects the constraint concept)
            if reversed_x > (MAX_INT - digit) // 10:
                return 0
                
            reversed_x = reversed_x * 10 + digit
        
        # Restore the sign
        reversed_x *= sign
        
        # Final strict check for the negative limit edge case
        if reversed_x < MIN_INT or reversed_x > MAX_INT:
            return 0
            
        return reversed_x
