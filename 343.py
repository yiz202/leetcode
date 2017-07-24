class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n <= 3: return n - 1
        # dp = [0] * (n + 1)
        # dp[2], dp[3] = 2, 3
        # for x in range(4, n + 1):
        #     dp[x] = max(3 * dp[x - 3], 2 * dp[x - 2])
        # return dp[n]

        if n == 2: return 1
        if n == 3: return 2
        if n % 3 == 0: return pow(3, n / 3)
        if n % 3 == 1:
            return 2 * 2 * pow(3, (n - 4) / 3)
        else:
            return 2 * pow(3, (n - 1) / 3)