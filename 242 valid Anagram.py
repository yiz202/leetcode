class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        cs = Counter(s)
        ct = Counter(t)
        for x in s:
            if cs[x] !=ct[x]: return False
        for y in t:
            if ct[y]!=cs[y]:return False
        return True