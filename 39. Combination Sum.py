from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Sorting helps us optimize by stopping early if a number exceeds the target
        candidates.sort()

        def backtrack(start_index, current_sum, current_path):
            # Base case: We found a valid combination
            if current_sum == target:
                res.append(current_path.copy())
                return
            
            # Iterate through the candidates starting from 'start_index'
            for i in range(start_index, len(candidates)):
                # Optimization: Since the array is sorted, if the current candidate
                # pushes the sum over the target, all subsequent candidates will too.
                if current_sum + candidates[i] > target:
                    break
                
                # Choose the candidate
                current_path.append(candidates[i])
                
                # Explore further (we pass 'i' and not 'i + 1' because we can reuse the same element)
                backtrack(i, current_sum + candidates[i], current_path)
                
                # Backtrack: Remove the candidate to try the next one
                current_path.pop()

        backtrack(0, 0, [])
        return res
