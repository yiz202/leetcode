class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
        # write your code here
        p = 0
        for i in range(len(num)-1,0,-1):
            if num[i-1] < num[i]:
                p = i-1
                break
            else:
                if i == 1:
                    return num[::-1]
        for i in range(len(num)-1,-1,-1):
            if num[i] > num[p]:
                num[i] , num[p] = num[p], num[i]
                break
        li = []
        for j in range(len(num)-1,p,-1):
            li.append(num[j])
        return num[:(p+1)]+li

