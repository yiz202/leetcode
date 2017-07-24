class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # if not triangle: return 0
        # dp = [[0]*i for i in range(1,len(triangle)+1)]
        # dp[0][0] = triangle[0][0]
        # for i in range(1,len(dp)):
        #     for j in range(i+1):
        #         if j ==0:
        #             dp[i][j] = triangle[i][j]+dp[i-1][j]
        #         elif j == i:
        #             dp[i][j] = triangle[i][j] + dp[i-1][j-1]
        #         else:

        #             dp[i][j] = min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
        # return min(dp[-1])