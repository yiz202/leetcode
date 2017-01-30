class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ds = {}
        for item in strs:
            if ''.join(sorted(item)) not in ds:
                ds[''.join(sorted(item))] = [item]
            else:
                ds[''.join(sorted(item))].append(item)
        return [ds[k] for k in ds]