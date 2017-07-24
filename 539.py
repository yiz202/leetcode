class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def convert(timePoints):
            minute = [int(time[:2])*60+int(time[3:]) for time in timePoints]
            minute.sort()
            return minute
        minute = convert(timePoints)
        # print minute
        # print minute[1:]+minute[:1]
        # print [(x-y)%(24*60) for x, y in zip(minute,minute[1:]+minute[:1])]
        return min((y-x)%(24*60) for x, y in zip(minute,minute[1:]+minute[:1]))