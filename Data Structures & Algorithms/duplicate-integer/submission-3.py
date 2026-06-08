class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_sort = sorted(nums)
        bflag = False
        if(len(nums_sort)>1):
            for i in range(0,len(nums)):
                if (nums_sort[i] == nums_sort[i-1]):
                    bflag = True
        return bflag        

            