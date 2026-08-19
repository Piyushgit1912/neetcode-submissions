class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price= float('inf')
        # max_profit=0
        profit=0
        for p in prices:
            if min_price<p:
                profit=profit+(p-min_price)
                min_price=p
            else:
                min_price=min(min_price,p)
            
        
        return profit