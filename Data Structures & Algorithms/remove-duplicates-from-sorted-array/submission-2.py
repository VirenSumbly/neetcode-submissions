class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=set(nums)
        sortedA=sorted(a)
        b=len(sortedA)
        nums[:b-1:1] = sortedA
        return b
        