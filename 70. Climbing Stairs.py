class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: 1 way for 1 step, 2 ways for 2 steps
        if n <= 2:
            return n
            
        # a represents ways(n-2), b represents ways(n-1)
        a, b = 1, 2
        
        # Calculate ways for steps 3 up to n
        for _ in range(3, n + 1):
            # The next step is the sum of the previous two
            a, b = b, a + b
            
        return b
