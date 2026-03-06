class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort to ensure duplicates are adjacent
        nums.sort()
        result = []
        subset = []
        
        def backtrack(start_index):
            # Append a copy of the current subset to the result
            result.append(subset[:])
            
            for i in range(start_index, len(nums)):
                # Skip duplicate elements to prevent duplicate subsets
                if i > start_index and nums[i] == nums[i - 1]:
                    continue
                
                # Include the current number and explore further
                subset.append(nums[i])
                backtrack(i + 1)
                
                # Backtrack by removing the recently added number
                subset.pop()
                
        backtrack(0)
        return result
