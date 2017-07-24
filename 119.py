class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0: return [1]

        prev = [1]
        for i in range(rowIndex):
            next = [1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1]
            prev = next
        return next


