from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Handle the edge case where input is empty
        if not digits:
            return []
        
        # Mapping of digits to letters as per telephone buttons
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index, current_str):
            # Base case: If the current string is the same length as digits,
            # we have a complete combination.
            if len(current_str) == len(digits):
                res.append(current_str)
                return
            
            # Get the current digit we are processing
            current_digit = digits[index]
            
            # Iterate over all letters corresponding to this digit
            for char in phone_map[current_digit]:
                # Recurse with the next index and the updated string
                backtrack(index + 1, current_str + char)
        
        # Initiate backtracking starting at index 0
        backtrack(0, "")
        
        return res
