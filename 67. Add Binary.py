class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize pointers at the end of each string
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        # Continue if there are unprocessed digits or a remaining carry
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            # Add integer value of the current character if the pointer is valid
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # Append the least significant bit of the total to the result list
            result.append(str(total % 2))
            
            # Carry over the most significant bit
            carry = total // 2

        # Reverse the collected characters and join into the final string
        return ''.join(result[::-1])
