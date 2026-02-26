class Solution:
    def mySqrt(self, x: int) -> int:
        # Handle base cases for 0 and 1
        if x < 2:
            return x
        
        # The square root of x (where x >= 2) is always <= x // 2
        left, right = 2, x // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            squared = mid * mid
            
            if squared == x:
                return mid
            elif squared < x:
                left = mid + 1
            else:
                right = mid - 1
                
        # Since the goal is the rounded-down square root, return 'right'
        # when the loop finishes and 'left' has surpassed 'right'
        return right
