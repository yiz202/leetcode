class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def check(grid, i, j):
            res = 0
            if i == 0 or grid[j][i - 1] == 0: res += 1
            if j == 0 or grid[j - 1][i] == 0: res += 1
            if i == len(grid[0]) - 1 or grid[j][i + 1] == 0: res += 1
            if j == len(grid) - 1 or grid[j + 1][i] == 0: res += 1
            return res

        y = len(grid)
        if y == 0: return 0
        x = len(grid[0])
        sum = 0
        res = 0
        for j in range(y):
            for i in range(x):
                if grid[j][i] == 1:
                    res += check(grid, i, j)
        return res



