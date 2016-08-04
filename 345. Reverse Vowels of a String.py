class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = ['a','e','i','o','u','A','E','I','O','U']
        li = []
        old = list(s)
        i,j = 0,len(s)-1
        while i<j:
            if old[i] not in v:i+=1
            if old[j] not in v:j-=1
            if old[i] in v and old[j] in v:
                old[i],old[j] = old[j],old[i]
                i+=1
                j-=1
        return "".join(old)
