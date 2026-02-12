class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        
        # 1. Whitespace: Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1
            
        # Check if we reached the end of the string after skipping spaces
        if i == n:
            return 0
        
        # 2. Signedness: Check for sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # 3. Conversion: Read digits
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            i += 1
        
        # Apply the sign
        num *= sign
        
        # 4. Rounding: Clamp to 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
            
        return num
