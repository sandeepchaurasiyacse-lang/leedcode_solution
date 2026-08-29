class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        last = nums[n-k:]
        first = nums[:n-k]
        nums[:] = last + first