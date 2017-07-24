class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key = lambda x:(-len(x),x))
        for w in d:
            i = 0
            for c in s:
                if i < len(w):
                    if c == w[i]:
                        i+=1
                else:
                    return w
        return ''
Solution().findLongestWord("aaa",
["aaa","aa","a"])