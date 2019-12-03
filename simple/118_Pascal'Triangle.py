class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            n = [1]*(i+1)
            if i >= 2:
                for j in range(1,i):
                   n[j] = p[j-1] + p[j]
            result.append(n)
            p = n
        return result