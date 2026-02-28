class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        
        # Process elements until the unclassified region is exhausted
        while mid <= high:
            if nums[mid] == 0:
                # Swap the 0 to the front
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 is in the correct middle section, just move the current pointer
                mid += 1
            else:
                # Swap the 2 to the back
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
