from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                # Skip duplicate branches: 
                # If current number is the same as previous and the previous is not in the current path,
                # then picking it would lead to a duplicate permutation.
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                    
                visited[i] = True
                path.append(nums[i])
                
                backtrack(path)
                
                # Backtrack
                path.pop()
                visited[i] = False
                
        backtrack([])
        return res
