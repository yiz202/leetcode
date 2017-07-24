class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        zero = one = 0
        for i in range(len(nums)):
            if nums[i] == 0: zero+=1
            elif nums[i] == 1: one+=1
            if i == 0: nums[i] = 0
            if zero == one:
                nums[i] = nums[i-1]+2
                res = max(nums[i],res)
            elif i!=0:
                nums[i] = nums[i-1]
        return res
Solution().findMaxLength([0,0,0,1,1,1,0])