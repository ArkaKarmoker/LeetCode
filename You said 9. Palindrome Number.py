class Solution:
    def isPalindrome(self, x: int) -> bool:
        # A negative number cannot be a palindrome (e.g., -121 -> 121-)
        if x < 0:
            return False
        
        # Convert to string and check if it equals its reverse
        return str(x) == str(x)[::-1]
