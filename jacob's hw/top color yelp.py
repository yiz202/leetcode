from collections import Counter
class Solution:
    def topColor(self, list):
        # dc = {}
        # for row in list:
        #     for color in row:
        #         if color not in dc:
        #             dc[color] = 1
        #         else:
        #             dc[color]+=1
        # res = []
        # most = 0
        # for color, occurance in dc.iteritems():
        #     most = max(most,occurance)
        # for color, occurance in dc.iteritems():
        #     if occurance == most:
        #         res.append(color)
        # return sorted(res)
        counter = Counter([color for row in list for color in row])
        return sorted([k for k, v in counter.items() if v == max(counter.values())])




