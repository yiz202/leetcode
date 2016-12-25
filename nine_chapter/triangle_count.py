class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        # write your code here
        S = sorted(S)
        res = 0

        for i,k in enumerate(S):
            left, right = 0, i-1
            while left< right:
                if S[left]+S[right] > k:
                    res+=right-left
                    right-=1
                else:
                    left+=1
        return res