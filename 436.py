# Definition for an interval.
from collections import defaultdict
import bisect
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        l = sorted((e.start, i) for i, e in enumerate(intervals))
        res = []
        for e in intervals:
            r = bisect.bisect_left(l, (e.end,))
            res.append(l[r][1] if r < len(l) else -1)
        return res
Solution().findRightInterval([Interval(3,4),Interval(2,3),Interval(1,2)])




