class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        p = len(s)-1
        for x in s:
            total+=26**p*(ord(x)-ord('A')+1)
            p-=1
        return total
            