class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if n < k: return []
        if n == k: return [[i for i in range(1, n + 1)]]
        if k == 1: return [[i] for i in range(1, n + 1)]

        for i in range(n, 1, -1):
            current = self.combine(i - 1, k - 1)
            for needone in current:
                needone.append(i)
                res.append(needone)
        return res



