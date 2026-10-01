class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posint = []
        negint = []
        res = []
        for i in nums:
            if i > 0:
                posint.append(i)
            else:
                negint.append(i)
        posint = posint[::-1]
        negint = negint[::-1]
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(posint.pop())
            else:
                res.append(negint.pop())
        return res