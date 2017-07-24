class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import defaultdict
        digit = defaultdict(int)
        part = defaultdict(str)
        k = 1
        for c in s:
            if c.isdigit():
                digit[k] = digit[k] * 10 + int(c)
            elif c.isalpha():
                part[k] += c
            elif c == '[':
                k += 1
            elif c == ']':
                part[k - 1] += digit[k - 1] * part[k]
                digit[k - 1] = 0
                part[k] = ''
                k -= 1

        return part[1]



Solution().decodeString("10[l]")