class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        
        def dfs(sub1: str, sub2: str) -> bool:
            # Base case: identical strings are trivially true
            if sub1 == sub2:
                return True
            
            # Check memoization cache
            state = (sub1, sub2)
            if state in memo:
                return memo[state]
            
            # Early pruning: strings with different characters cannot be scrambled
            if sorted(sub1) != sorted(sub2):
                memo[state] = False
                return False
            
            n = len(sub1)
            
            # Try splitting the string at every possible index from 1 to n - 1
            for i in range(1, n):
                # Case 1: Substrings are NOT swapped
                # Left part of sub1 matches left part of sub2 AND right matches right
                if dfs(sub1[:i], sub2[:i]) and dfs(sub1[i:], sub2[i:]):
                    memo[state] = True
                    return True
                
                # Case 2: Substrings ARE swapped
                # Left part of sub1 matches right part of sub2 AND right matches left
                if dfs(sub1[:i], sub2[-i:]) and dfs(sub1[i:], sub2[:-i]):
                    memo[state] = True
                    return True
            
            # If no valid split is found, mark as false and return
            memo[state] = False
            return False
            
        return dfs(s1, s2)
