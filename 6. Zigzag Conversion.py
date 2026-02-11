class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If 1 row or rows >= length, no zigzag needed
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize a list of empty strings for each row
        rows = [''] * numRows
        
        current_row = 0
        step = 1  # 1 means moving down, -1 means moving up
        
        for char in s:
            rows[current_row] += char
            
            # If we hit the top or bottom, reverse the step direction
            if current_row == 0:
                step = 1
            elif current_row == numRows - 1:
                step = -1
            
            current_row += step
            
        # Join all rows to form the final string
        return ''.join(rows)
