from collections import Counter
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        # Pruning 1: If the word is longer than the board's total cells, it's impossible.
        if len(word) > rows * cols:
            return False
            
        # Pruning 2: Check if the board has enough of each character to form the word.
        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False
                
        # Pruning 3: Reverse the word if the starting character is more frequent than the ending character.
        # This forces the DFS to start with the less frequent character, minimizing early branching.
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]
            
        def dfs(r: int, c: int, index: int) -> bool:
            # All characters have been matched
            if index == len(word):
                return True
                
            # Out of bounds or character mismatch
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                board[r][c] != word[index]):
                return False
                
            # Temporarily mark the current cell as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all 4 adjacent directions
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
                     
            # Backtrack: Restore the cell's original value
            board[r][c] = temp
            
            return found

        # Iterate through the grid to find the starting letter
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
                        
        return False
