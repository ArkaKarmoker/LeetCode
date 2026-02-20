class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        result = "1"
        
        # We need to generate the next string n - 1 times
        for _ in range(n - 1):
            next_result = []
            count = 1
            
            # Iterate through the current string to apply Run-Length Encoding
            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    # If the current character is the same as the previous, increment count
                    count += 1
                else:
                    # If it changes, append the count and the previous character
                    next_result.append(str(count))
                    next_result.append(result[i - 1])
                    count = 1 # Reset count for the new character
            
            # Don't forget to append the final run of characters
            next_result.append(str(count))
            next_result.append(result[-1])
            
            # Update the result for the next iteration
            result = "".join(next_result)
            
        return result
