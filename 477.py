class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = 1
        res = 0
        size = len(nums)
        for i in range(32):
            bitcount = 0
            for n in nums:
                bitcount += (n >> i) & 1
            res += bitcount * (size - bitcount)
        return res

