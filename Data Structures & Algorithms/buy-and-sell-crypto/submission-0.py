class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a,b = 0,1
        profit = 0
        while b<len(prices):
            if prices[a]<prices[b]:
                diff = prices[b]-prices[a]
                profit = max(diff,profit)
            else:
                a = b
            b+=1
        return profit    
        

        
        