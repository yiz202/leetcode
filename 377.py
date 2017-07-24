# class Solution(object):
#     def combinationSum4(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         res = []
#         # sublist = []
#         for i, ele in enumerate(nums):
#             if ele == target: res += [[ele]]
#             if ele < target:
#                 sublist = self.combinationSum4(nums, target - ele)
#                 for li in sublist:
#                     res.append([ele] + li)
#             else:
#                 break
#
#         return res
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # using memorization search recursion
        # memo = [-1]*(target+1)
        # memo[0] = 1

        # def helper(nums,target):
        #     if memo[target]!=-1:
        #         return memo[target]
        #     res = 0
        #     for ele in nums:
        #         if ele == target:
        #             res+=1
        #         if ele<target:
        #             res+=helper(nums,target-ele)
        #     memo[target] = res
        #     return res
        # return helper(nums,target)


        # using dp
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(len(dp)):
            for number in nums:
                if number < i:
                    dp[i] += dp[i - number]
                if number == i:
                    dp[i] += 1
        return dp[target]


print Solution().combinationSum4([2,1],3)