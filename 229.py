class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        n1 = n2 = None
        c1 = c2 = 0
        for item in nums:
            if item == n1 or c1 == 0 and item!=n2:
                n1 = item
                c1+=1
            elif item == n2 or c2 == 0 and item!=n1:
                n2 = item
                c2+=1
            else:
                c1-=1
                c2-=1



        if n1 is not None and sum([x==n1 for x in nums]) > len(nums)*1.0/3:
            ans.append(n1)
        if n1!= n2:
            if n2 is not None and sum([x==n2 for x in nums]) > len(nums)*1.0/3:
                ans.append(n2)

        return ans



if __name__ == '__main__':
    Solution().majorityElement([1,2,2,3,2,1,1,3])