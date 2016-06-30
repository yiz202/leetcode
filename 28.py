class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        idx2 = 0
        start = 0
        idx1 = 0
        if haystack == "" and needle == "": return 0
        if needle == "": return 0
        if haystack == "": return -1
        if len(haystack) < len(needle): return -1
        while idx1 < len(haystack):
            while idx2< len(needle):
                if haystack[idx1] == needle[idx2]:
                    idx2+=1
                    idx1+=1
                else:
                    start+=1
                    idx1 = start
                    if start == len(haystack): return -1
                    idx2 = 0
                if idx2 == len(needle): return start

                break


        return -1
if __name__ == '__main__':
    Solution().strStr("mississippi","issi")