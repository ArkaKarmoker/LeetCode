class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize pointers
        left = 0
        right = len(height) - 1
        max_water = 0
        
        # Loop until pointers meet
        while left < right:
            # Calculate current width
            width = right - left
            
            # Find the limiting height for the container
            current_height = min(height[left], height[right])
            
            # Calculate area and update maximum if current is larger
            current_area = width * current_height
            max_water = max(max_water, current_area)
            
            # Move the pointer of the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
