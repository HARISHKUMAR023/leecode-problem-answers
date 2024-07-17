class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        mini=prices[0]
        for i in prices:
           c=i-mini
           maxp = max(maxp,c)
           mini = min(mini,i)
        return maxp
