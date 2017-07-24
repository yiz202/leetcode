class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if s == '': return []
        res = []
        countsum = 0
        ls = len(s)
        lp = len(p)
        if lp > ls: return []
        dp = collections.defaultdict(int)
        ds = collections.defaultdict(int)
        for elemP in p:
            dp[elemP] += 1
        for i in range(lp):
            ds[s[i]] += 1
        if ds == dp: res.append(0)
        for i in range(lp, ls):
            ds[s[i]] += 1
            ds[s[i - lp]] -= 1
            if ds[s[i - lp]] == 0:
                del ds[s[i - lp]]
            if ds == dp: res.append(i - lp + 1)
        return res

# 以上为n方做法，接下来是n的做法

