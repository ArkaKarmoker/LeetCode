from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the candidates first. 
        # This is crucial for easily skipping duplicates and optimizing the search.
        candidates.sort()
        res = []

        def backtrack(start_idx: int, current_target: int, path: List[int]):
            # Base case: if we hit exactly 0, we found a valid combination
            if current_target == 0:
                res.append(path[:]) # Append a copy of the current path
                return
            
            for i in range(start_idx, len(candidates)):
                # Skip duplicate elements at the same depth level of the recursion tree
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                
                # Pruning step: Since the array is sorted, if the current number 
                # is strictly greater than the remaining target, all subsequent 
                # numbers will also be greater. We can safely stop exploring this branch.
                if candidates[i] > current_target:
                    break
                
                # Include the current number and move forward
                path.append(candidates[i])
                
                # Recurse with the next index (i + 1) because we can't reuse the same element
                backtrack(i + 1, current_target - candidates[i], path)
                
                # Backtrack: remove the number to try the next possible candidate
                path.pop()

        backtrack(0, target, [])
        return res
