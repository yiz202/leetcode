class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # if not nums: return []
        # li = [0]*len(nums)
        # res1 = [0]*len(nums)
        # res2 = [0]*len(nums)
        # for i in range(len(nums)):
        #     if i == 0: res1[i] = 1
        #     else: res1[i]=nums[i-1]*res1[i-1]
        # for i in range(len(nums)-1,-1,-1):
        #     if i == len(nums)-1: res2[i] = 1
        #     else:res2[i]=nums[i+1]*res2[i+1]
        # for i in range(len(nums)):
        #     li[i] = res1[i]*res2[i]
        # return li

        size = len(nums)
        output = [1] * size
        left = 1
        for x in range(size - 1):
            left *= nums[x]
            output[x + 1] *= left
        right = 1
        for x in range(size - 1, 0, -1):
            right *= nums[x]
            output[x - 1] *= right
        return output

