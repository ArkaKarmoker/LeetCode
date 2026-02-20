import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Dictionaries of sets to keep track of seen numbers
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)  # key: (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == '.':
                    continue
                
                # Check if the value already exists in the current row, col, or box
                box_coord = (r // 3, c // 3)
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_coord]):
                    return False
                
                # Add the value to our tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_coord].add(val)
                
        return True
