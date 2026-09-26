class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        h = {}
        for i in nums:
            if i not in h:
                h[i] = 1
            elif i in h:
                h[i] += 1
        print(h)
        for i in h:
            if h[i] > len(nums)/2:
                return i
        


        