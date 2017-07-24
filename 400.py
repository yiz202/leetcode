class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        length = 1
        start = 1

        while n > length * 9 * start:
            n -= length * 9 * start
            length += 1
            start *= 10
        start += (n - 1) / length
        num = str(start)
        return int(num[(n - 1) % length])

