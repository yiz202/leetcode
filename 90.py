class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        if len(nums) == 1: return [[], nums]
        beforeset = self.subsetsWithDup(nums[:-1])
        for before in beforeset:
            res.append(before)
            if before + [nums[-1]] not in beforeset:
                res.append(before + [nums[-1]])
        return res


