class Solution:
    def romanToInt(self, s: str) -> int:
        # Map roman symbols to their integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # Check if current value is less than the next value
            # Ensure i + 1 is within bounds
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i+1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
                
        return total
