class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array to use the two-pointer approach
        nums.sort()
        n = len(nums)
        
        # Initialize closest_sum with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        # Iterate through the array, stopping 2 elements before the end
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If the current sum is closer to the target than the previous closest, update it
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # If we hit the target exactly, we can't get closer than 0 distance
                if current_sum == target:
                    return current_sum
                
                # If sum is too small, move left pointer to increase sum
                elif current_sum < target:
                    left += 1
                
                # If sum is too large, move right pointer to decrease sum
                else:
                    right -= 1
                    
        return closest_sum
