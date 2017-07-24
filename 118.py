class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []

        res = [[1]]
        for i in range(numRows - 1):
            row = [1] + [res[-1][j] + res[-1][j + 1] for j in range(len(res[-1]) - 1)] + [1]
            res.append(row)
        return res
