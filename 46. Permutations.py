class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(start):
            # Base case: if start index reaches the end, a permutation is complete
            if start == len(nums):
                res.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                # Swap the current element to the start position
                nums[start], nums[i] = nums[i], nums[start]
                
                # Recursively generate permutations for the rest of the array
                backtrack(start + 1)
                
                # Backtrack: undo the swap to restore the original array state
                nums[start], nums[i] = nums[i], nums[start]
                
        backtrack(0)
        return res
