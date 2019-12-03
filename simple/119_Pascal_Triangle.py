class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        for i in range(rowIndex+1):
            n = [1]*(i+1)
            if i >= 2:
                for j in range(1,i):
                    n[j] = p[j-1] + p[j]
            p = n
            
        return n