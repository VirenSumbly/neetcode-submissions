class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = []
        for i in range(len(nums2)-1,-1,-1):
            if len(stack) == 0:
                result.append(-1)
            elif len(stack) != 0 and stack[-1] > nums2[i]:
                result.append(stack[-1])
            elif len(stack) != 0 and stack[-1] <= nums2[i]:
                while len(stack) != 0 and stack[-1] <= nums2[i]:
                    stack.pop()
                if len(stack) == 0:
                    result.append(-1)
                else:
                    result.append(stack[-1])
            stack.append(nums2[i])
        print(result[::-1])
        result = result[::-1]
        result2=[]
        for i in nums1:
            result2.append(result[nums2.index(i)])
        print(result2)
        return result2   