class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []  # Stores indices of the bars
        
        # Iterate one step past the end to ensure all remaining bars in the stack are processed
        for i in range(len(heights) + 1):
            # Treat the out-of-bounds height as 0 to force popping everything left in the stack
            current_height = heights[i] if i < len(heights) else 0
            
            # Maintain a monotonic increasing stack
            while stack and heights[stack[-1]] > current_height:
                h = heights[stack.pop()]
                
                # Calculate width
                # If stack is empty, the popped bar was the shortest seen so far, spanning from index 0 to i.
                # Otherwise, it spans from the index after the new top of the stack up to i - 1.
                w = i if not stack else i - stack[-1] - 1
                
                # Update the maximum area found
                max_area = max(max_area, h * w)
                
            stack.append(i)
            
        return max_area
