class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # low = 1
        # high = len(nums)-1
        # while low < high:
        #     count = 0
        #     mid = (low+high)/2
        #     for n in nums:
        #         if n <= mid:
        #             count+=1
        #     if count > mid:
        #         high = mid
        #     else:
        #         low = mid+1
        # return low
        slow, fast = 0, 0
        p = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        while True:
            p = nums[p]
            slow = nums[slow]
            if slow == p:
                break
        return slow
