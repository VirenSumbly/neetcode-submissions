class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for r in range(1,len(nums)):
            if nums[r] != nums[l]:
                nums[l+1] = nums[r]
                l+=1
            else:
                continue
        return l+1
        