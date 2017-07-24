class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.s = set()
        self.s.add(n)

        def computeRes(n):
            res = 0
            while n:
                producedDigit = n % 10
                res += producedDigit ** 2
                n /= 10
            if res in self.s: return False
            self.s.add(res)
            if res != 1:
                computeRes(res)
            else:
                return True


        return computeRes(n)
Solution().isHappy(2)