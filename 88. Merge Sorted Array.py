class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers for the last elements of nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # Pointer for the last position of the merged array
        p = m + n - 1
        
        # Compare elements from the back and place the largest at the current end position
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            
        # If there are leftover elements in nums2, copy them over
        # (Any leftover elements in nums1 are already in their correct places)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
