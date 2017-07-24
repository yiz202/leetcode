class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        new = ''
        ROMAN = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        while num:
            ran = []
            for i in ROMAN.keys():
                if num / i >= 1:
                    continue
                else:
                    ran.append(i - 1)
                    ran.append(i)
            if num <= (ran[0] + ran[1]) / 2:
                new += ROMAN[ran[0]]
                num -= ran[0]
            else:
                new += ROMAN[ran[1]]
                num -= ran[1]
        return new


Solution().intToRoman(1)