class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        
        for num in nums:
            # Keep the element if it's one of the first two elements, 
            # or if it's different from the element two steps back.
            if slow < 2 or num != nums[slow - 2]:
                nums[slow] = num
                slow += 1
                
        return slow
