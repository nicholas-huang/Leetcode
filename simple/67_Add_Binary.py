class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        r, p = '',0
        d = len(a) - len(b)
        a = '0'*-d +a
        b = '0'*d +b
        for i,j in zip(a[::-1],b[::-1]):
            s = int(i) + int(j) +p
            r = str(s%2) + r
            p = s//2
        
        return '1' + r if p else r