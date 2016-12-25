class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        res = []
        for idx, item in enumerate(nums):
            p1 = nums[:idx]
            p2 = nums[idx+1:]
            for perm in self.permute(p1+p2):
                perm.append(item)
                res.append(perm)
        return res
print Solution().permute([1,2,3])