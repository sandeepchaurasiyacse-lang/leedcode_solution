class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        low = 0
        high = m
        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i
            if i == 0:
                a = float('-inf')
            else:
                a = nums1[i - 1]
            if i == m:
                b = float('inf')
            else:
                b = nums1[i]
            if j == 0:
                c = float('-inf')
            else:
                c = nums2[j - 1]
            if j == n:
                d = float('inf')
            else:
                d = nums2[j]
            if a <= d and c <= b:
                if (m + n) % 2 == 1:
                    return max(a, c)
                return (max(a, c) + min(b, d)) / 2.0
            elif a > d:
                high = i - 1
            else:
                low = i + 1