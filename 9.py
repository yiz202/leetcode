class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x< 0: return False
        y = abs(x)
        z,num = 0,y
        while y:
            z = z*10+y%10
            y/=10
        return z==num
            
        