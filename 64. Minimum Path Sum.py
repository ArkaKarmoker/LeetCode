class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # Update the first row (can only be reached from the left)
        for j in range(1, cols):
            grid[0][j] += grid[0][j - 1]
            
        # Update the first column (can only be reached from above)
        for i in range(1, rows):
            grid[i][0] += grid[i - 1][0]
            
        # Update the rest of the grid with the minimum path sum to reach each cell
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                
        # The bottom-right cell contains the minimum path sum for the entire grid
        return grid[-1][-1]
