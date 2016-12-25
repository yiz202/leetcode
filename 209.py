class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        minlen = len(nums) + 1
        left, right, sum = 0, 0, 0
        while right <= len(nums) and left <= right:
            if sum < s:
                sum += nums[right]
                right += 1
            else:
                minlen = min(minlen, right - left)
                sum -= nums[left]
                left += 1
        return minlen if minlen <= len(nums) else 0


if __name__ == '__main__':
    Solution().minSubArrayLen(4,[1,4,4])