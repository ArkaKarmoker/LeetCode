from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initialize the result list with the empty subset
        result = [[]]
        
        # Iteratively build subsets by adding the current number to existing subsets
        for num in nums:
            result.extend([curr + [num] for curr in result])
            
        return result
