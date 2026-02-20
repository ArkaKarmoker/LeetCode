from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Sets to keep track of numbers used in rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        empty_cells = []
        
        # Initialize the sets with the current board state and find all empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    box_idx = (r // 3) * 3 + c // 3
                    boxes[box_idx].add(val)
                    
        def backtrack(index: int) -> bool:
            # If we have filled all empty cells, the puzzle is solved
            if index == len(empty_cells):
                return True
            
            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + c // 3
            
            # Try placing digits 1 through 9
            for val in map(str, range(1, 10)):
                if val not in rows[r] and val not in cols[c] and val not in boxes[box_idx]:
                    # Place the digit
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
                    
                    # Move to the next empty cell
                    if backtrack(index + 1):
                        return True
                        
                    # Backtrack: undo the placement if it doesn't lead to a solution
                    board[r][c] = '.'
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[box_idx].remove(val)
            
            # Trigger backtracking to the previous state
            return False
            
        # Start backtracking from the first empty cell
        backtrack(0)
