class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums2 = []
        for i in range(len(nums)):
            if nums[i] != val:
                nums2.append(nums[i])
        nums[:2:1] = nums2
        return len(nums2)

        