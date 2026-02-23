class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        solutions = []
        state = []
        
        def backtrack(row: int, col_mask: int, diag1_mask: int, diag2_mask: int) -> None:
            # Base case: All queens have been placed successfully
            if row == n:
                # Convert the sequence of column indices into the required string format
                board = ["." * col + "Q" + "." * (n - col - 1) for col in state]
                solutions.append(board)
                return
            
            # Get a bitmask representing available positions in the current row.
            # 1 means available, 0 means under attack.
            available_positions = ((1 << n) - 1) & ~(col_mask | diag1_mask | diag2_mask)
            
            while available_positions:
                # Extract the rightmost 1-bit (the first available spot)
                pos = available_positions & -available_positions
                
                # Turn off that 1-bit to mark it as visited for the loop
                available_positions &= available_positions - 1
                
                # Calculate the exact column index (0-indexed) from the bit position
                col = pos.bit_length() - 1
                state.append(col)
                
                # Recurse to the next row. Update the attack zones:
                # - col_mask: add the current position
                # - diag1_mask: add position and shift left (represents down-right diagonal)
                # - diag2_mask: add position and shift right (represents down-left diagonal)
                backtrack(
                    row + 1, 
                    col_mask | pos, 
                    (diag1_mask | pos) << 1, 
                    (diag2_mask | pos) >> 1
                )
                
                # Backtrack by removing the choice
                state.pop()
                
        backtrack(0, 0, 0, 0)
        return solutions
