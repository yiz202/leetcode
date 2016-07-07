class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dicp = {}
        dics = {}
        str = str.split()
        pattern = list(pattern)
        if len(pattern) != len(str): return False
        for i in range(len(pattern)):
            if pattern[i] not in dicp:
                dicp[pattern[i]] = str[i]
            else:
                if str[i]!= dicp[pattern[i]]:
                    return False
            if str[i] not in dics:
                dics[str[i]] = pattern[i]
            else:
                if pattern[i]!= dics[str[i]]:
                    return False
        return True

