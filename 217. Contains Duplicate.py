class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 0
            else:

                dic[n]+=1
                if dic[n] == 1:
                    return True
        return False
                