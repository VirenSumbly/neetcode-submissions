class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_sort = sorted(nums)
        if len(nums_sort) > 1:
            for i in range(len(nums)):
                if nums_sort[i] == nums_sort[i-1]:
                    return True
        return False

        