class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        partitionIndex, changeIndex = -1, -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                partitionIndex = i - 1
                break
        if partitionIndex != -1:
            for i in range(len(nums) - 1, 0, -1):
                if nums[i] > nums[partitionIndex]:
                    changeIndex = i
                    nums[i], nums[partitionIndex] = nums[partitionIndex], nums[i]
                    break

            nums[partitionIndex+1:] = reversed(nums[partitionIndex+1:])
            return
        nums[:] = reversed(nums)


Solution().nextPermutation([1,2])