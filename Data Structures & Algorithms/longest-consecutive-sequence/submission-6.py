class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # Check if this number is the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                # Start counting the consecutive numbers
                while (n + length) in numSet:
                    length += 1
                # Update the longest sequence found so far
                longest = max(longest, length)
        
        return longest