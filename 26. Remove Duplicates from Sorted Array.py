class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0 or size == 1: return size
        i,j = 0,1
        while j < size:
            if nums[j] == nums[i]:
                j+=1
            else:
                i+=1
                nums[i] = nums[j]
        return i+1
            