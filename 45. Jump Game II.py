class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_end = 0
        farthest = 0
        
        # loop up to the second to last element
        # since reaching the last index means I'm done
        for i in range(len(nums) - 1):
            # keep track of the max distance reachable
            farthest = max(farthest, i + nums[i])
            
            # if the current index reaches the edge of the current jump's range
            # I have to make a jump to continue
            if i == curr_end:
                jumps += 1
                curr_end = farthest
                
                # slight optimization: if the new end already reaches or passes the last index, break early
                if curr_end >= len(nums) - 1:
                    break
                    
        return jumps
