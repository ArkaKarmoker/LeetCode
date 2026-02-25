class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a DP array for the first row, where there's only 1 way to reach each cell
        row = [1] * n
        
        # Iterate through the remaining grid row by row
        for _ in range(1, m):
            for j in range(1, n):
                # The number of paths to current cell is paths from the top + paths from the left
                # row[j] currently holds the top value, row[j-1] holds the left value
                row[j] += row[j - 1]
                
        return row[n - 1]
