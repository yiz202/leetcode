class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        if s == "":
            return -1
        ds = collections.Counter(s)
        for i, letter in enumerate(s):
            if ds[letter] == 1:
                return i
            if i == len(s)-1: return -1
        