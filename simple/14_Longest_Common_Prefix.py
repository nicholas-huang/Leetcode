class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs :
            return ""
        res = strs[0]
        for i in range(len(strs)):
            while strs[i].find(res) !=0:
                res = res[0:-1]
        return res