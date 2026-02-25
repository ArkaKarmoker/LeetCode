from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # If the starting cell has an obstacle, no paths are possible
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
            
        cols = len(obstacleGrid[0])
        dp = [0] * cols
        
        # Base case: 1 path to the starting position
        dp[0] = 1 
        
        for row in obstacleGrid:
            for j in range(cols):
                if row[j] == 1:
                    # Obstacle found, path is blocked
                    dp[j] = 0
                elif j > 0:
                    # Add paths coming from the left cell
                    # dp[j] already contains the paths from the top cell
                    dp[j] += dp[j - 1]
                    
        return dp[-1]
