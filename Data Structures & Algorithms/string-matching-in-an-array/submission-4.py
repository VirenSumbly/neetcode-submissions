class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for i in words:
            for j in words:
                if i in j and i != j and len(i) < len(j):
                    ans.add(i)
        return list(ans)
        