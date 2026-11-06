class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hs = set()
        for i in nums:
            if i in hs:
                return int(i)
            hs.add(i)
            
        