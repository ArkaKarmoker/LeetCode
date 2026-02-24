from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize an n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Set the initial boundaries
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        # The value to be filled into the matrix
        num = 1
        
        # Loop until all n^2 elements are filled
        while num <= n * n:
            # Traverse from left to right along the top boundary
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1  # Constrict top boundary
            
            # Traverse from top to bottom along the right boundary
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1  # Constrict right boundary
            
            # Traverse from right to left along the bottom boundary
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1  # Constrict bottom boundary
            
            # Traverse from bottom to top along the left boundary
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1  # Constrict left boundary
            
        return matrix
