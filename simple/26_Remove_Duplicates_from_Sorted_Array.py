class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        flag = 1
        for i in range(1,len(nums)):
            if nums[i]!= nums[i-1]:
                nums[flag] = nums[i]
                flag+=1
        return flag