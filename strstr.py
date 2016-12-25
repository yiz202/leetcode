class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == None or needle == None:
            return -1
        lenS = len(haystack)
        lenT = len(needle)
        for i in range(lenS-lenT+1):
            j=0
            for j in range(lenT):
                if haystack[i+j]!= needle[j]:
                    break
            if j == lenT-1:
                return i
        return -1


if __name__ == '__main__':
    Solution().strStr("","")