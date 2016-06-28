class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        li = []
        if numRows == 1: return s
        for k in range(numRows):
            i = k
            while i < len(s):
                li.append(s[i])
                if k!=0 and k!=numRows-1:
                    j = i+(numRows-k-1)*2
                    if j < len(s):
                        li.append(s[j])
                i+= (numRows-1)*2
        return "".join(li)





if __name__ == '__main__':
    Solution().convert("AB",4)