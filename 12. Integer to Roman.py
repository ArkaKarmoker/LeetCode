class Solution:
    def intToRoman(self, num: int) -> str:
        # List of tuples mapping integer values to their Roman numeral strings.
        # It allows us to handle special subtractive cases (like 900, 400, 90, etc.)
        # exactly the same way we handle normal cases.
        value_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        result = []
        
        # Iterate through each symbol, starting from the largest
        for value, symbol in value_map:
            # If the input number is 0, we are done
            if num == 0:
                break
            
            # Determine how many times the current symbol fits into num
            # count gives the number of times we append the symbol
            # num becomes the remainder
            count, num = divmod(num, value)
            
            # Append the symbol 'count' times
            result.append(symbol * count)
            
        return "".join(result)
