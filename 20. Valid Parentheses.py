class Solution:
    def isValid(self, s: str) -> bool:
        # Quick check: odd length strings can never be valid
        if len(s) % 2 != 0:
            return False
            
        stack = []
        # Map closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element if stack is not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # The mapping for the current closing bracket must match the popped element
                if bracket_map[char] != top_element:
                    return False
            else:
                # It is an opening bracket, push to stack
                stack.append(char)

        # If the stack is empty, return True, otherwise False
        return not stack
