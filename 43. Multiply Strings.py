class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: if either number is zero, the result is zero
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        # The maximum possible length of the product is m + n
        res = [0] * (m + n)
        
        # Traverse both strings from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Multiply current digits
                mul = int(num1[i]) * int(num2[j])
                
                # Positions in the result array
                p1, p2 = i + j, i + j + 1
                
                # Add the current product to the existing value at p2 (which might have a carry)
                total = mul + res[p2]
                
                # Update the current position and add the new carry to the next position left
                res[p2] = total % 10
                res[p1] += total // 10
                
        # Skip leading zeros (there could be at most one leading zero in this approach)
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
            
        # Convert the remaining numbers back to a string
        return "".join(map(str, res[start:]))
