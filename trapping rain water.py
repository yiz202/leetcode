from heapq import heappop,heappush
class Solution:
    # @param heights: a matrix of integers
    # @return: an integer
    def trapRainWater(self, heights):
        # write your code here
        m,n = len(heights),len(heights[0])
        if m == 0 or n == 0:
            return 0
        visited = [ 0 for i in range(n) for j in range(m)]
        point = [(0,1),(0,-1),(1,0),(0,1)]
        mh = []
        for i in range(m):
            heappush(mh,(heights[i][0],i,0))
            heappush(mh,(heights[i][n-1],i,0))
        for j in range(n):
            heappush(mh,(heights[0][j],0,j))
            heappush(mh,(heights[m-1][j],m-1,j))
        total = 0
        while mh:
            min_height,i,j = heappop(mh)
            for dx,dy in point:
                i += dx
                j+=dy
                if 0 <= i < m and 0<= j < n and visited[i][j] == 0:
                    visited[i][j] =1
                    newh = heights[i][j]
                    to_b_pushed = max(newh,min_height)
                    if min_height > newh:
                        total+= min_height-newh
        return total


if __name__ == '__main__':
    Solution().trapRainWater([[12,13,0,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]])