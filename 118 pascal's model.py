class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0: return []
        res = [[1]]
        while numRows>1:
            newRow = [1] + [res[-1][i] + res[-1][i+1] for i in range(len(res[-1])-1)] + [1]
            res.append(newRow)
            numRows-=1
        return res





        