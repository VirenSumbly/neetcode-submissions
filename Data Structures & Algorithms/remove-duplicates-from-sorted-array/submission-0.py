class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if i not in res:
                res.append(i)
        print(res)
        unique=len(set(nums))
        print(unique)
        nums[:unique-1:1] = res
        return unique
