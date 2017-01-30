import heapq as f
class Solution:
    # @param {int[][]} arrays a list of array
    # @param {int} k an integer
    # @return {int} an integer, K-th largest element in N arrays
    def KthInArrays(self, arrays, k):
        # Write your code here
        q = []
        for arr in arrays:
            for item in arr:
                f.heappush(q,item)
                if len(q)> k: f.heappop(q)
        return q[0]