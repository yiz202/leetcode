class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = "122"
        p = 2
        res = 0
        while len(s) < n:
            s += int(s[p]) * str(3 - int(s[-1]))
            p += 1
        for i in s[:n]:
            if i == '1':
                res += 1
        return res




