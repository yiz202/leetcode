class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while n/26 > 0:
            res.append(chr(ord('A')+(n-1)%26))
            n=(n-1)/26
        res.append(chr(ord('A')-1+n))
        return ''.join(res[::-1])


Solution().convertToTitle(26)