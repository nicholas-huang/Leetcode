class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # abs(x)
        n =  x if x>0 else -x
        result = 0
        while n!=0:
            result = result*10 + n%10
            n = n/10
            #判别是否溢出
            if result > 0x7fffffff:
                return 0
        return result if x>0 else -result