class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        sums = 0
        while num >9:
            sums+= num%10
            num/=10
            if num < 10:
                num +=sums
                sums = 0
        return num


if __name__ == '__main__':
    Solution().addDigits(19)