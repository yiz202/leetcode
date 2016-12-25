class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        import collections
        dr = collections.Counter(ransomNote)
        dm = collections.Counter(magazine)
        for k in dr:
            if k not in dm: return False
            dm[k]-=dr[k]
            if dm[k] < 0: return False
        return True
        