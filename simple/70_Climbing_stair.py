class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        dip = [0]*n
        dip[0] = 1
        dip[1] = 2
        for i in range(2,n):
            dip[i] = dip[i-1] + dip[i-2]
        return dip[n-1]