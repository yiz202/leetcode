class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cache = {}

        def helper(nums, curNum, res):
            if not nums: return []
            curHolder = []
            key = tuple(nums)
            if key in cache:
                return cache[key]
            for i, n in enumerate(nums):
                if curNum == None:
                    curNum = n
                elif n >= curNum:
                    curHolder += helper(nums[i + 1:], n, res)
                    res.append(curHolder)
            cache[key] = curHolder
            return curHolder

        res = []
        helper(nums, None, res)
Solution().findSubsequences([4,6,7,7])