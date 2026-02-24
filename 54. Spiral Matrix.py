class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        if not matrix or not matrix[0]:
            return res
            
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while left <= right and top <= bottom:
            # Move from left to right across the top boundary
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1
            
            # Move from top to bottom down the right boundary
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            # Check if there's still a bottom boundary to traverse
            if top <= bottom:
                # Move from right to left across the bottom boundary
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            
            # Check if there's still a left boundary to traverse
            if left <= right:
                # Move from bottom to top up the left boundary
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
                
        return res
