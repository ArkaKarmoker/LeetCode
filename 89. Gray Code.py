class Solution:
    def grayCode(self, n: int) -> List[int]:
        # The i-th Gray code is mathematically derived using: i ^ (i >> 1)
        # Iterate through 0 to (2^n) - 1 to build the complete sequence
        return [i ^ (i >> 1) for i in range(1 << n)]
