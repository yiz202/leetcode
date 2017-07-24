class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid - 1] > nums[mid]:
                end = mid
            elif nums[mid + 1] > nums[mid]:
                start = mid
            elif nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
        if nums[start] > nums[end]:
            return start
        else:
            return end
print Solution().findPeakElement([3,2,1])