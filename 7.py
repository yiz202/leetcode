class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = abs(x)
        if y <=10: return x
        res = 0
        while y !=0:
            d = y/10
            m = y%10
            y = d
            res = res*10+m
        if x < 0: return 0-res
        return res
if __name__ == '__main__':
    Solution().reverse(-123)