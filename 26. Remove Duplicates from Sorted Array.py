class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # If the array is empty, there are 0 unique elements
        if not nums:
            return 0
        
        # k represents the position for the next unique element 
        # and the total number of unique elements found so far.
        k = 1 
        
        # Iterate from the second element to the end
        for i in range(1, len(nums)):
            # If the current element is different from the previous one,
            # it's a new unique element.
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]  # Place it at the k-th index
                k += 1             # Increment k for the next unique element
                
        return k
