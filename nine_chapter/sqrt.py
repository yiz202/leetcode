class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        left = 0
        right = x
        while left+1< right:
            mid = (right+left)/2
            if mid**2 == x : return mid
            if mid**2 > x:
                right = mid
            if mid**2 < x:
                left = mid
        if left**2 ==x: return left
        if right**2== x: return right
        if right**2 < x: return right

if __name__ == '__main__':
    Solution().sqrt(999999999)