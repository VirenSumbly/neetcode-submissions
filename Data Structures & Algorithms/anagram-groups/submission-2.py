from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            si=tuple(sorted(i))
            if si not in d:
                #h[si] = []
                d[si].append(i)
            elif si in d:
                d[si].append(i)
        return list(d.values())

        