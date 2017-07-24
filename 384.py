class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.num = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.num

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums = self.num[:]
        for i in range(len(nums) - 1, 0, -1):
            p = random.randrange(0, i + 1)
            nums[i], nums[p] = nums[p], nums[i]
        return nums



        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.reset()
        # param_2 = obj.shuffle()