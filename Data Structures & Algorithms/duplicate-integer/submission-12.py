class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for i in nums:
            if i not in h:
                h[i] = 1
            elif i in h:
                h[i] +=1

        #print(h)
        for i in h.values():
            if i != 1:
                return True
        return False
        