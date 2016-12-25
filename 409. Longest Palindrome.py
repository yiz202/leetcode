class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        odd = 0

        ds = collections.Counter(s)
        for key in ds:
            if ds[key]%2 == 1: odd+=1
        return len(s) if odd == 0 else len(s)-odd+1
            