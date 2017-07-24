class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cache = {}
        def solve(nums):
            if len(nums) == 1: return nums[0]
            key = tuple(nums)
            if key in cache:
                return cache[key]
            else:
                print '1'
                ans = max(nums[0]-solve(nums[1:]),nums[-1]-solve(nums[:-1]))
                cache[key] = ans
                return ans
        return solve(nums)>=0