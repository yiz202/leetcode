class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
"""
        dic = {}
        for i in range(len(nums)):
            # if nums[i] not in dic:
            a = target- nums[i]
            if a in dic.values():
                for key, value in dic.iteritems():
                    if value == target-nums[i]:
                        print "dsfsdf{}".format([key,i])
                        return [key,i]
            dic[i] = nums[i]




if __name__ == '__main__':
    Solution().twoSum([3,2,4],6)