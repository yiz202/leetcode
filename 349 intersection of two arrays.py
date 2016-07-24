class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        # for i in nums1:
        #     for j in nums2:
        #         if i == j and i not in result: result.append(i)
        # return result

        # nums1 = set(nums1)
        # res = []
        # for num in nums1:
        #     if num in nums2:
        #         res.append(num)
        # return res
        return list(set(nums1) & set(nums2))
