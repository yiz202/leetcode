class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        commonstr = ''
        if len(strs) == 0: return commonstr
        for i, s in enumerate(strs[0]):
            for str in strs[1:]:
                if i >= len(str) - 1 or str[i] != s[i]:
                    return commonstr
            commonstr += s[i]
            print commonstr


Solution().longestCommonPrefix(["abab","aba","abc"])