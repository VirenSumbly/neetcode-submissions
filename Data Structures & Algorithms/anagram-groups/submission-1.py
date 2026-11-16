class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for i in strs:
            si=tuple(sorted(i))
            if si not in h:
                h[si] = []
                h[si].append(i)
            elif si in h:
                h[si].append(i)
        return list(h.values())

        