class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                diff = max(diff,prices[j]-prices[i])
        print(diff)
        return diff