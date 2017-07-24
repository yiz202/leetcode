class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(k,chooseFrom,s,res,possible):
            if k == 0:
                for item in chooseFrom:
                    if item > s:
                        return
                    if item == s:
                        # possible.append(item)
                        res.append(possible+[item])
                        return
                return
            for i,num in enumerate(chooseFrom):
                # possible.append(num)
                helper(k-1,chooseFrom[i+1:],s-num,res,possible+[num])
                # possible.pop()
        res,possible = [],[]
        helper(k-1,range(1,10),n,res,possible)
        return res

print Solution().combinationSum3(3,7)