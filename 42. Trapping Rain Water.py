class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
            
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        water_trapped = 0
        
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                water_trapped += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                water_trapped += r_max - height[r]
                
        return water_trapped
