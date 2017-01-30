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



Solution().subsets([1,2,3])