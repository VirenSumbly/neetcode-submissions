class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if d not in h:
                h[nums[i]] = i
            elif d in h:
                return [h[target-nums[i]],i]
            