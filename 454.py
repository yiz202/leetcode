class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        d = {}
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                a = A[i]
                b = B[i]
                if A[i] + B[i] not in d:
                    d[A[i] + B[i]] = 1
                else:
                    d[A[i] + B[i]] += 1
            print d
            for i in range(len(C)):
                for j in range(len(D)):
                    if -1 * (C[i] + D[i]) in d:
                        res += d[-1 * (C[i] + D[i])]
        return res

Solution().fourSumCount([1,2],
[-2,-1],
[-1,2],
[0,2])