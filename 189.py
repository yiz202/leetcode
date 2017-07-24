class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, in1, in2):
            while in1 < in2:
                nums[in1], nums[in2] = nums[in2], nums[in1]
                in1 += 1
                in2 -= 1

        n = len(nums)
        k = k % n

        reverse(nums, 0, n - 1)

        reverse(nums, 0, k - 1)

        reverse(nums, k, n - 1)


