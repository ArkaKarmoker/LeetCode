class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        target = len(nums) - 1
        
        for i, jump in enumerate(nums):
            # If the current index is beyond the furthest reachable point,
            # it's impossible to move forward.
            if i > max_reach:
                return False
            
            # Update the furthest point that can be reached
            if i + jump > max_reach:
                max_reach = i + jump
            
            # If the last index is already reachable, stop early
            if max_reach >= target:
                return True
                
        return False
