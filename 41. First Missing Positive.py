from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Place each valid number in its correct index (i.e., number 'x' at index 'x-1')
        for i in range(n):
            # While the number is within our target range [1, n] 
            # AND it is not already sitting at its correct index...
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap the current number to its correct spot
                # Note: We assign it to a variable first to avoid Python's tuple unpacking evaluation order bug
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Step 2: Find the first missing positive integer
        for i in range(n):
            # If the number at index 'i' is not 'i + 1', then 'i + 1' is missing
            if nums[i] != i + 1:
                return i + 1
                
        # Step 3: If all numbers 1 through n are present, the missing number is n + 1
        return n + 1
