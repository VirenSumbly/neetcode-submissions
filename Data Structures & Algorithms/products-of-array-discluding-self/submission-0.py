class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        prod = 1
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if (i == j):
                    continue
                else:
                    prod *=nums[j]
            final.append(prod)
            prod = 1
        return final

        