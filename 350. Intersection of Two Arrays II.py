class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        if len(nums1) >  len(nums2):
            nums1,nums2 = nums2,nums1
        c = collections.Counter(nums1)
        for i in nums2:
            if c[i]>0:
                result.append(i)
                c[i]-=1


        return result


            