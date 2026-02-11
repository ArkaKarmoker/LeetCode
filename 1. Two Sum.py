class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store value: index
        prev_map = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            
            # Check if the difference is already in the map
            if diff in prev_map:
                return [prev_map[diff], i]
            
            # If not, store the current number and index
            prev_map[n] = i
