class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, current_comb: List[int]) -> None:
            # Base case: A valid combination of size k has been formed
            if len(current_comb) == k:
                result.append(current_comb.copy())
                return
            
            # Optimization: Prune branches that lack enough remaining elements
            # Elements still needed = k - len(current_comb)
            # Maximum valid starting number = n - (elements needed) + 1
            # Add 1 extra because Python's range stop index is exclusive
            stop_limit = n - (k - len(current_comb)) + 2
            
            for i in range(start, stop_limit):
                current_comb.append(i)
                backtrack(i + 1, current_comb)
                current_comb.pop() # Backtrack to explore other possibilities

        backtrack(1, [])
        return result
