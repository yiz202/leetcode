class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i, j = 0, len(s) - 1
        while i < j:
            while s[i] not in v and i < j: i += 1
            while s[j] not in v and i < j: j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s
Solution().reverseVowels('hello')


