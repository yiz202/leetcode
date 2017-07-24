class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """

        def leftToright(n):
            if n == 1:
                return 1
            return 2 * rightToleft(n / 2)

        def rightToleft(n):
            if n == 1:
                return 1
            if n % 2:
                return 2 * leftToright((n - 1) / 2)
            else:
                return 2 * leftToright(n / 2) - 1

        return leftToright(n)
Solution().lastRemaining(4)