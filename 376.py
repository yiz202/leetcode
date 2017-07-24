class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        res = 0
        while i < len(nums) - 1:
            print i
            if nums[i] > nums[i + 1]:
                res += 1
                while nums[i] > nums[i + 1] and i < len(nums) - 1: i += 1
            elif nums[i] == nums[i + 1]:
                i += 1
            elif nums[i] < nums[i + 1]:
                res += 1
                while nums[i] < nums[i + 1] and i < len(nums) - 1: i += 1
        return res


Solution().wiggleMaxLength([1,7,4,9,2,5])