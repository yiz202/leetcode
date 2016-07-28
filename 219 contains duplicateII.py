class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = i
            else:
                if abs(i-dict[nums[i]]) <=k and i !=dict[nums[i]]:
                    return True
                dict[nums[i]] = i
        return False

