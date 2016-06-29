class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        j = 0
        sign = 1
        if str == "": return 0
        str = str.strip()
        num = 0
        i = 0
        while i < len(str):
            if str[i] == "-":
                sign = -1
                j+=1
                i+=1
            elif str[i] == "+":
                sign = 1
                j+=1
                i+=1
            elif not str[i].isdigit(): break
            else:
                num = num*10+int(str[i])
                if sign == -1:
                    if num >=(1<<31): return -(1<<31)
                elif sign == 1:
                    if num >= (1<<31)-1: return (1<<31)-1
                i+=1
        if j>1: return 0
        return sign*num













if __name__ == '__main__':
    Solution().myAtoi("-21")


    # MaxInt = (1 << 31) - 1