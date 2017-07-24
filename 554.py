class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        d = collections.defaultdict(int)
        mx = 0
        for w in wall:
            sum = 0
            for ele in w[:-1]:
                sum+=ele
                d[sum]+=1
                mx = max(d[sum],mx)
        return len(wall)-mx