__author__ = 'zhangyilun'
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        a,b,c = m-1,n-1,m+n-1
        for i in range(c,-1,-1):
            if a == -1:
                nums1[i] = nums2[b]
                b-=1
            while a>=0 and b >=0:

                if nums1[a] >= nums2[b]:
                    nums1[i] = nums1[a]
                    a-=1
                else:
                    nums1[i] = nums2[b]
                    b-=1
                break

            # elif b == -1:
            #     nums1[i] = nums1[a]
            #     a-=1

if __name__ == '__main__':
    Solution().merge([2,0],1,[1],1)
