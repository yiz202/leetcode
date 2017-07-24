class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            s = 0
            for n in nums:
                s += (n >> i) & 1
            rem = s % 3
            if i == 31 and rem:
                res -= 1 << 31
            else:
                res |= rem << i
        return res




Solution().singleNumber([3,3,3,-200])