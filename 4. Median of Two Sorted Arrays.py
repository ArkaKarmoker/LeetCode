class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = (total + 1) // 2
        
        # Ensure A is the smaller array so we binary search on the smaller range
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A)
        
        while l <= r:
            i = (l + r) // 2 # Partition index for A
            j = half - i     # Partition index for B
            
            # Determine edge values. 
            # Use -infinity for left edges if index is 0
            # Use +infinity for right edges if index is at the end
            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < len(A) else float("inf")
            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < len(B) else float("inf")
            
            # Check if the partition is valid
            if A_left <= B_right and B_left <= A_right:
                # Valid partition found
                if total % 2:
                    # Odd: The median is the max of the left elements
                    return float(max(A_left, B_left))
                else:
                    # Even: Average of the max of lefts and min of rights
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            
            elif A_left > B_right:
                # A_left is too big, need to reduce size of A's left partition
                r = i - 1
            else:
                # B_left is too big, need to increase size of A's left partition
                l = i + 1
