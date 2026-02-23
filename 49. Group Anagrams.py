from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map to group strings by their sorted tuple representation
        anagram_map = defaultdict(list)
        
        for s in strs:
            # A sorted tuple of characters acts as a unique key for anagrams
            anagram_map[tuple(sorted(s))].append(s)
            
        return list(anagram_map.values())
