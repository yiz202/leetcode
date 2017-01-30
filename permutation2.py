class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """


        def getPermuteArr(arr):
            res = []
            if n == 1: return [[1]]
            for i, e in enumerate(arr):
                for before in getPermuteArr(arr[:i] + arr[i +1:]):
                    before = [e] + [before]
                    res.append(before)
            return res

        res = getPermuteArr(range(1,n+1))
        return ''.join([str(x) for x in res[k - 1]])
Solution().getPermutation(2,1)