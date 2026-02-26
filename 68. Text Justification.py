from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        curr_line = []
        curr_length = 0
        
        for word in words:
            # Check if adding the current word exceeds maxWidth
            # len(curr_line) represents the minimum number of spaces needed between words
            if curr_length + len(word) + len(curr_line) > maxWidth:
                total_spaces = maxWidth - curr_length
                
                # Single word on a line: left-justify
                if len(curr_line) == 1:
                    result.append(curr_line[0] + ' ' * total_spaces)
                else:
                    # Multiple words: distribute spaces evenly, extra spaces to the left
                    gaps = len(curr_line) - 1
                    base_space, extra_space = divmod(total_spaces, gaps)
                    
                    # Distribute extra spaces to the leftmost gaps
                    for i in range(extra_space):
                        curr_line[i] += ' '
                        
                    separator = ' ' * base_space
                    result.append(separator.join(curr_line))
                
                # Reset tracking variables for the next line
                curr_line = []
                curr_length = 0
            
            curr_line.append(word)
            curr_length += len(word)
            
        # Process the final line (must be left-justified)
        last_line = ' '.join(curr_line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result
