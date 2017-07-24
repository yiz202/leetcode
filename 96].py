class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] * dp[n - i]
        return sum(dp)


print Solution().numTrees(1)