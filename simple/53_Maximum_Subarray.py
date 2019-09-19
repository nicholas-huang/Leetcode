class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        tmp = nums[0]
        max_ = tmp
        for i in range(1,n):
            if tmp + nums[i] > nums[i]:
                max_ = max(max_,tmp+nums[i])
                tmp = tmp + nums[i]
            else:
                max_ = max(max_,tmp,tmp+nums[i],nums[i])
                tmp= nums[i]
        return max_