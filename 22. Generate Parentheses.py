class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        # backtrack function to build the string
        def backtrack(current_str, open_count, close_count):
            # Base Case: If the string has reached the maximum length (2 * n)
            # it means we have a valid combination.
            if len(current_str) == 2 * n:
                result.append(current_str)
                return

            # Decision 1: Add an open parenthesis if we still have some left
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
            
            # Decision 2: Add a close parenthesis if it's valid to do so
            # (must have more open ones than closed ones so far)
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)

        # Start the recursion
        backtrack("", 0, 0)
        return result
