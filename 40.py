class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def search(nums,target,res,possible):
            for i,e in enumerate(nums):
                if e < target:
                    search(nums[i+1:],target-e,res,possible+[e])
                elif e == target:
                    res.append(possible+[e])
                else:
                    continue
            return
        res = []
        possible = []
        search(candidates,target,res,possible)
        return res
Solution().combinationSum2([10,1,2,7,6,1,5],8)