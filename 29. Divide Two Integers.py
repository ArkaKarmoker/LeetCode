class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define 32-bit integer limits
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648 # -2**31
        
        # 1. Handle strict overflow edge case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
            
        # 2. Determine the sign of the result
        # True if one is negative and the other is positive (XOR operator)
        is_negative = (dividend < 0) ^ (divisor < 0)
        
        # 3. Work with absolute values to simplify logic
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        
        # 4. Subtract largest possible multiples of the divisor
        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            multiple = 1
            
            # Keep multiplying by 2 (using bitwise left shift << 1) 
            # as long as it fits into the remaining dividend
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
                
            # Subtract the large multiple from the dividend
            abs_dividend -= temp_divisor
            # Add the number of times we multiplied to the quotient
            quotient += multiple
            
        # 5. Apply the correct sign
        if is_negative:
            quotient = -quotient
            
        # 6. Clamp the result to 32-bit signed integer boundaries
        return min(max(MIN_INT, quotient), MAX_INT)
