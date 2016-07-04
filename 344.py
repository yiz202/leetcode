class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        li = []
        for i in range(len(s)-1,-1,-1):
            li.append(s[i])
        return "".join(li)