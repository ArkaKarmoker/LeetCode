class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_exponent = False
        seen_dot = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in "+-":
                # Sign is only valid at the start or directly after 'e'/'E'
                if i > 0 and s[i - 1] not in "eE":
                    return False
            elif char in "eE":
                # Exponent is valid only if a digit was seen and no prior exponent exists
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                # Reset seen_digit because we need digits *after* the exponent
                seen_digit = False
            elif char == ".":
                # Dot is valid only if no prior dot or exponent exists
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                # Any other character is invalid
                return False
                
        # The number is valid if it properly ends with a digit
        return seen_digit
