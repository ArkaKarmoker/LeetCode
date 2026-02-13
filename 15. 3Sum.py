class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n):
            # Optimization: If the current number is positive, we cannot sum to 0
            # because the array is sorted and remaining numbers will also be positive.
            if nums[i] > 0:
                break
                
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Two pointer initialization
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # Found a triplet
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the second element (left pointer)
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                        
                    # Skip duplicates for the third element (right pointer)
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                        
        return res
