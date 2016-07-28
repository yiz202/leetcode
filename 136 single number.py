class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = nums[0]
        for i in range(1,len(nums),1):
            left = left ^ nums[i]
        return left