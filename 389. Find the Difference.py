class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letter = {}
        for c in s:
            letter[c] = letter[c]+1 if c in letter else 1
        for c in t:
            if c not in letter: return c
            letter[c]-=1
            if letter[c] < 0: return c


