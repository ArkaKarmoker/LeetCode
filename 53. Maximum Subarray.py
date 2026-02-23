from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize variables with the first element to handle all-negative arrays correctly
        current_sum = nums[0]
        max_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Decide to either add to the running sum or start a new subarray
            current_sum = max(num, current_sum + num)
            
            # Update the global maximum sum found so far
            max_sum = max(max_sum, current_sum)
            
        return max_sum
