from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    bound = mid
                    # If looking for the first occurrence, keep searching to the left
                    if is_first:
                        right = mid - 1
                    # If looking for the last occurrence, keep searching to the right
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound
            
        # Find the first occurrence
        first_pos = find_bound(True)
        
        # If the target is not in the array, no need to search for the last position
        if first_pos == -1:
            return [-1, -1]
            
        # Find the last occurrence
        last_pos = find_bound(False)
        
        return [first_pos, last_pos]
