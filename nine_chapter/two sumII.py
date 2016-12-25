class Solution:
    # @param nums, an array of integer
    # @param target, an integer
    # @return an integer
    def twoSum2(self, nums, target):
        # Write your code here
        res = 0
        left,right = 0, len(nums)-1
        nums = sorted(nums)

        while left < right:
            if nums[left]+nums[right] > target:
                res+= right-left
                right-=1
            else:
                left+=1
        return res



            