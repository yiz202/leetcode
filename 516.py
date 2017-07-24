class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {}

        def findseq(ia, ib):
            if (ia, ib) in cache:
                return cache[(ia, ib)]
            a = s[ia]
            b = s[ib]
            if ia == ib: return 1
            if ia > ib: return 0
            if a == b:
                cache[(ia, ib)] = 2 + findseq(ia + 1, ib - 1)
                return cache[(ia, ib)]
            else:
                cache[(ia, ib)] = max(findseq(ia, ib - 1), findseq(ia + 1, ib))
                return cache[(ia, ib)]

        return findseq(0, len(s) - 1)


Solution().longestPalindromeSubseq('abab')