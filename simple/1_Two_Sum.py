class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic =dict()
        for index, value in enumerate(nums):
            if target - value in dic:
                return [dic[target-value],index]
            else:
                dic[value] = index