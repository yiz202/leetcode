class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        d = {}

        def solve(idx, num):
            if not num: return 1
            accu = 0
            key = idx, tuple(num)
            if key in d:
                return d[key]
            for i, n in enumerate(num):
                if idx % n == 0 or n % idx == 0:
                    accu += solve(idx + 1, num[:i] + num[i + 1:])
            d[key] = accu
            return accu

        solve(1, range(1, N + 1))
Solution().countArrangement(3)







Solution().countArrangement(2)