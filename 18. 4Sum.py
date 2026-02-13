class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 3):
            # 1. Avoid duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # 2. Pruning for i
            # If current smallest sum is greater than target, no need to continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # If current largest sum is less than target, this i is too small, try next
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
            
            for j in range(i + 1, n - 2):
                # 3. Avoid duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # 4. Pruning for j
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                
                # 5. Two-pointer approach for the remaining two numbers
                left, right = j + 1, n - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for left and right
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                        
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
                        
        return res
