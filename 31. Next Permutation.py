from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        
        # Step 1: Find the first decreasing element from the right (the pivot)
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        # Step 2: If a pivot was found, find the element just larger than it to its right
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap the pivot with this larger element
            nums[i], nums[j] = nums[j], nums[i]
            
        # Step 3: Reverse the elements to the right of the pivot
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
