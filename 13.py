class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i = 0
        sum = 0
        if s == "": return 0
        while i < len(s)-1:
            if ROMAN[s[i]] < ROMAN[s[i+1]]:
                sum-=ROMAN[s[i]]
            else:
                sum+=ROMAN[s[i]]
            i+=1
        sum+=ROMAN[s[i]]

        return sum




