class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 5
        res = 0
        while x <= n:
            res += n / x
            x *= 5
        return res

