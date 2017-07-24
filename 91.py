class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0': return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):
            if s[i] != '0':
                dp[i] = dp[i - 1]
            if int(s[i - 1]) * 10 + int(s[i]) > 10 and int(s[i - 1]) * 10 + int(s[i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]


Solution().numDecodings('10')