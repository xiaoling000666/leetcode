class Solution(object):
    def maxProfit(self, prices):
        maxprofit = 0
        for i in range(1,len(prices)):
            if prices[i]-prices[i-1]>0:
                maxprofit +=prices[i]-prices[i-1]
        return maxprofit
price = [7,1,5,3,6,4]
print
