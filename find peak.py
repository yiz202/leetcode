class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        l = 0
        r = len(A)
        while l < r:
            i = (l+r)/2
            print "mid{} at {}".format(A[i],i)

            if A[i] < A[i+1]:
                l = i
                print"left {} at{}".format(A[l],l)
            elif A[i] < A[i-1]:
                r = i
                print"right {} at{}".format(A[r],r)
            elif A[i]> A[i-1] and A[i]>A[i+1]: return i



if __name__ == '__main__':
    Solution().findPeak([1,2,3,4,10,9,5,9,5,9,5,10,9,8,7,5])