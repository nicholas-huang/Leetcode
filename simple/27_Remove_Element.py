class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        flag = 0
        for i in range(len(nums)):
            if nums[i]!= val:
                nums[flag]= nums[i]
                flag+=1
        return flag