class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        first_col_zero = False
        
        # Step 1: Use first row and column as markers.
        for r in range(rows):
            # Check if the first column has any zeroes
            if matrix[r][0] == 0:
                first_col_zero = True
                
            # Check the rest of the columns
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
                    
        # Step 2: Set matrix cells to zero based on the markers.
        # Start from 1 to avoid modifying the markers prematurely.
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
                    
        # Step 3: Handle the first row.
        if matrix[0][0] == 0:
            for c in range(cols):
                matrix[0][c] = 0
                
        # Step 4: Handle the first column.
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0
