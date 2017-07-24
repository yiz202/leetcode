class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1: return [[], nums]
        res = []

        beforeset = self.subsets(nums[:-1])

        for before in beforeset:
            res.append(before)
            res.append(before + [nums[-1]])
        return res
        # res = [[]]
        # for num in sorted(nums):
        #     res += [item + [num] for item in res]
        # return res


Solution().subsets([1,2,3,4])

# class Solution(object):
#     def subsets(self, nums):
#         res = []
#         self.dfs(nums, 0, [], res)
#         return res
#
#     def dfs(self, nums, index, path, res):
#         res.append(path)
#         for i in xrange(index, len(nums)):
#             self.dfs(nums, i + 1, path + [nums[i]], res)
# Solution().subsets([1,2,3])