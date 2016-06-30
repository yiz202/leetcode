class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        dic = {}

        l = 1<<31-1
        small = ""
        if not strs:return ""
        if len(strs) == 1: return strs[0]
        for s in strs:
            if len(s) < l:
                l = len(s)
        dic = {}
        for i in range(l):
            dic[i] = strs[0][i]
        for i in range(l):
            for s in strs[1:]:
                if s[i] != dic[i]:return small
            small+=s[i]
        return small







if __name__ == '__main__':
    Solution().longestCommonPrefix(["a","b"])