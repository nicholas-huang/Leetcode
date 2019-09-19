class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        pre_string = '1'
        for i in range(1,n):
            next_string, num, count = '', pre_string[0], 1
            for j in range(1,len(pre_string)):
                if pre_string[j] == num: count+=1
                else:
                    next_string += str(count)+num
                    num = pre_string[j]
                    count =1
            next_string += str(count) + num
            pre_string = next_string
        return pre_string
