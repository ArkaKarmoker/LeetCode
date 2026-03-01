from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        
        # Initialize DP arrays
        left = [0] * cols
        right = [cols] * cols
        height = [0] * cols
        
        max_area = 0

        for row in matrix:
            cur_left = 0
            cur_right = cols

            # Update height
            for j in range(cols):
                if row[j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            # Update left boundary
            for j in range(cols):
                if row[j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1

            # Update right boundary
            for j in range(cols - 1, -1, -1):
                if row[j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = cols
                    cur_right = j

            # Calculate the maximum area for the current row
            for j in range(cols):
                current_area = (right[j] - left[j]) * height[j]
                if current_area > max_area:
                    max_area = current_area

        return max_area
