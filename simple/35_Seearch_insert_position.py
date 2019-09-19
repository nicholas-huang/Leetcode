class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        if target > nums[-1]:
            return size
        left = 0
        right = size - 1
        while left < right:
            mid = left + (right - left)/2
            if target > nums[mid]:
                left = mid +1
            else:
                right = mid
        return left