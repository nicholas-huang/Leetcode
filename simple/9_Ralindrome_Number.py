class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #负数和10为因子的数
        if x < 0 or (x%10 == 0 and x !=0):
            return False
        re_num=0
        while(x>re_num):
            re_num = re_num*10 + x%10
            x = x/10
        
        return x == re_num or x == re_num/10