class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        def helper(num, k):
            if len(num) == 1: return str(num[0])
            v = math.factorial(len(num) - 1)
            first = k / v + 1
            return num[first - 1] + helper(num[:first - 1] + num[first - 1:], k % v + 1)

        return helper([str(i) for i in range(1, n + 1)], k)


Solution().getPermutation(2,1)