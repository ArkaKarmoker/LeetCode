class Solution:
    def numDecodings(self, s: str) -> int:
        # A string starting with '0' cannot be decoded
        if not s or s[0] == "0":
            return 0

        # prev_two represents dp[i-2] (ways to decode up to two characters ago)
        # prev_one represents dp[i-1] (ways to decode up to the previous character)
        prev_two = 1
        prev_one = 1

        for i in range(1, len(s)):
            current = 0
            
            # Check if a single-digit decode is possible (digit is 1-9)
            if s[i] != "0":
                current += prev_one
            
            # Check if a two-digit decode is possible (number is 10-26)
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev_two
            
            # Shift the window forward for the next iteration
            prev_two = prev_one
            prev_one = current
            
        return prev_one
