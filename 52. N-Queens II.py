class Solution:
    def totalNQueens(self, n: int) -> int:
        def solve(row: int, cols: int, diag1: int, diag2: int) -> int:
            # All queens placed successfully
            if row == n:
                return 1
            
            count = 0
            # Mask to keep only the valid n bits (ignoring bits beyond the board)
            mask = (1 << n) - 1
            
            # 1s represent available positions, 0s represent attacked positions
            available = mask & ~(cols | diag1 | diag2)
            
            while available:
                # Isolate the rightmost available position (lowest set bit)
                pos = available & -available
                
                # Clear this position from available choices for the current loop
                available &= available - 1
                
                # Recurse to the next row with updated attack vectors
                count += solve(
                    row + 1,
                    cols | pos,
                    (diag1 | pos) << 1,
                    (diag2 | pos) >> 1
                )
                
            return count

        return solve(0, 0, 0, 0)
