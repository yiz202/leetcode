class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == -1: return 1 / x
        if n == 0: return 1
        if n == 1: return x
        subp = self.myPow(x, n / 2)
        modp = self.myPow(x, n % 2)
        print subp ** 2 * modp
        return subp ** 2 * modp

Solution().myPow(2,16)