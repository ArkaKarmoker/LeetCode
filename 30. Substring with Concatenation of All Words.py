from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        n = len(s)
        
        # If the string is shorter than the required total length, it's impossible
        if n < total_len:
            return []
            
        word_freq = Counter(words)
        result = []
        
        # We only need to iterate `word_len` times to cover all possible word alignments
        for i in range(word_len):
            left = i
            right = i
            current_freq = Counter()
            words_used = 0
            
            while right + word_len <= n:
                # Extract the current word of length `word_len`
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_freq:
                    current_freq[word] += 1
                    words_used += 1
                    
                    # If we have more occurrences of 'word' than needed, slide the left pointer forward
                    while current_freq[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        current_freq[left_word] -= 1
                        words_used -= 1
                        left += word_len
                        
                    # If we have exactly the right number of words, record the start index
                    if words_used == word_count:
                        result.append(left)
                else:
                    # Invalid word encountered: completely reset the window
                    current_freq.clear()
                    words_used = 0
                    left = right
                    
        return result
