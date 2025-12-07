class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to minimize binary search range
        # This guarantees O(log(min(M, N))) which satisfies O(log(M+N))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        
        # Binary Search on the smaller array (nums1)
        left, right = 0, m
        
        while True:
            # i is the partition index for nums1
            i = (left + right) // 2
            # j is the calculated partition index for nums2
            j = half - i
            
            # Handle edge cases where partition is at the start or end of arrays
            # If i is 0, we use -infinity (left side is empty)
            # If i is m, we use +infinity (right side is empty)
            nums1_left = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < m else float('inf')
            
            nums2_left = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')
            
            # Check if we found the correct partition
            # We need max(Left Part) <= min(Right Part)
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # If the total number of elements is odd, the median is the smallest 
                # element on the right side (because we partition so right has the extra element)
                if total % 2:
                    return min(nums1_right, nums2_right)
                # If even, it is the average of the largest on left and smallest on right
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            
            # If nums1's left part is too large, move partition to the left
            elif nums1_left > nums2_right:
                right = i - 1
            # If nums1's left part is too small, move partition to the right
            else:
                left = i + 1