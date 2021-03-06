class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True]*max(2,n)
        isPrime[0],isPrime[1] = False,False
        x = 2
        while x * x < n:
            if isPrime[x*x]:
                p = x*x
            while p < n:
                isPrime[p] =False
                p+=x
            x+=1
        return sum(isPrime)