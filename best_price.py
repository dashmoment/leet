"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""
"""
class Solution:
    def bestprofit(self, prices):

        best_p = 0
        window = 2
        stride = 1
        
        while window <= len(prices):
            init = 0 
            while init + window < len(prices) + 1:
                sub_win = prices[init: init+window]
                
                if sub_win[-1] - sub_win[0]  > best_p:
                    best_p = sub_win[-1] - sub_win[0]
                    print(best_p)
                init = init+stride
            window = window + 1
        
        return best_p
"""

class Solution:
    def bestprofit(self, prices):

        minprice = prices[0]
        maxprofit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice

        return maxprofit


s = Solution()
print(s.bestprofit([7,1,5,3,6,4]))
