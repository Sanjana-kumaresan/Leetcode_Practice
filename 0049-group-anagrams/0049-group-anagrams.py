from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for s in strs: d[tuple(sorted(s))].append(s)
        return list(d.values())