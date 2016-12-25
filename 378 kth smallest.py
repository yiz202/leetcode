from heapq import heappop, heappush
class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        from heapq import heappop,heappush
        # write your code here
        m,n = len(matrix),len(matrix[0])
        visited = [[False] *n for _ in range(m)]
        q = [(matrix[0][0],0,0)]
        visited[0][0] = True
        for _ in range(k):
            ans,i,j = heappop(q)
            if i+1<m and visited[i+1][j] == False:
                heappush(q,(matrix[i+1][j],i+1,j))
                visited[i+1][j] = True
            if j+1<n and visited[i][j+1] == False:
                heappush(q,(matrix[i][j+1],i,j+1))
                visited[i][j+1] = True
        return ans
        
        
        
        
            
        
        