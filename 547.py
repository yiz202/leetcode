class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        def dfs(row):
            print row
            for friendIndex, friendship in enumerate(row):
                if friendship:
                    if friendIndex not in seen:
                        seen.add(friendIndex)
                        dfs(M[friendIndex])

        seen = set()
        m = len(M[0]) - 1
        n = len(M) - 1
        ans = 0
        for i in range(n + 1):
            if i not in seen:
                seen.add(i)
                dfs(M[i])
                ans += 1
        return ans
