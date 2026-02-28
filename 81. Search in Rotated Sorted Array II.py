class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
            
            # Handle the edge case where duplicates prevent identifying the sorted half
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
                
            # Left half is strictly sorted
            elif nums[left] <= nums[mid]:
                # Target is within the strictly sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Target must be in the right half
                else:
                    left = mid + 1
                    
            # Right half is strictly sorted
            else:
                # Target is within the strictly sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Target must be in the left half
                else:
                    right = mid - 1
                    
        return False
