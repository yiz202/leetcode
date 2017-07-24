class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        bucket = (len(s) + 1) * ['']
        d = {}
        for l in s:
            if l not in d:
                d[l] = 1
            else:
                d[l] += 1
        dlist = d.items()
        for tup in dlist:
            bucket[tup[1]] += tup[0] * tup[1]
        for i in range(len(bucket) - 1, 0, -1):
            if bucket[i] != '':
                res += bucket[i]
        return res



print Solution().frequencySort('eeeaaa')