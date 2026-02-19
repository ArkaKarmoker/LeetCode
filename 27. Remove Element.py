from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k will keep track of the number of valid elements 
        # and the index to place the next valid element.
        k = 0 
        
        # i iterates through all items in the array.
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k
