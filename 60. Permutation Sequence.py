class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Array to store available numbers: [1, 2, ..., n]
        numbers = []
        fact = 1
        
        # Precompute (n-1)! and populate the numbers array
        for i in range(1, n):
            fact *= i
            numbers.append(str(i))
        numbers.append(str(n))
        
        # Convert k to a 0-based index to make math operations align cleanly
        k -= 1
        result = []
        
        # Build the permutation digit by digit
        for i in range(n - 1, -1, -1):
            # Determine the index of the next number to pick
            idx = k // fact
            result.append(numbers.pop(idx))
            
            # Update k to reflect the remainder for the next positions
            k %= fact
            
            # Decrease the factorial for the next iteration (i.e., (n-2)!, (n-3)!)
            if i > 0:
                fact //= i
                
        return "".join(result)
