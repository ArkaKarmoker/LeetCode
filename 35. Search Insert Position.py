from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # If we find the target, return its index
            if nums[mid] == target:
                return mid
            
            # If target is greater, ignore left half
            elif nums[mid] < target:
                left = mid + 1
                
            # If target is smaller, ignore right half
            else:
                right = mid - 1
                
        # If the target is not found, 'left' will be at the correct insertion index
        return left
